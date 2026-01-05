CREATE TABLE flights (
    flight_id INTEGER PRIMARY KEY,
    airline TEXT,
    source TEXT,
    destination TEXT,
    departure_time TEXT,
    arrival_time TEXT,
    duration REAL,
    stops INTEGER
);
