import pandas as pd
import sqlite3

flights = pd.read_csv('../data/flight_price.csv')
conn = sqlite3.connect('../database/flight_pricing.db')
flights.to_sql('flights', conn, if_exists='replace', index=False)
conn.close()

print(flights.dtypes)