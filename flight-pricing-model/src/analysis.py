import pandas as pd
import sqlite3
import pickle
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns

conn = sqlite3.connect('../database/flight_pricing.db')
flights = pd.read_sql('SELECT * FROM flights', conn)
conn.close()

flights.dropna(inplace=True)
flights = pd.get_dummies(flights, columns = ['airline','source_city','destination_city'])


sns.histplot(flights['price'])
sns.lineplot(x='days_left', y='price', data=flights)
plt.show()

## Model building

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import root_mean_squared_error, r2_score

X = flights[['duration','days_left']]
y = flights['price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LinearRegression()
model.fit(X_train, y_train)

preds = model.predict(X_test)
print("RMSE:", root_mean_squared_error(y_test, preds))
print("R²:", r2_score(y_test, preds))

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models" / "linear_regression.pkl"

MODEL_PATH.parent.mkdir(exist_ok=True)

with open(MODEL_PATH, "wb") as f:
    pickle.dump(model, f)