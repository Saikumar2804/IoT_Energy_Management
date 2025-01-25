import sqlite3

class DatabaseHandler:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
    
    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS SensorData (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            site_id TEXT NOT NULL,
            meter_id TEXT NOT NULL,
            timestamp DATETIME NOT NULL,
            sensor_name TEXT NOT NULL,
            sensor_value REAL NOT NULL,
            status TEXT NOT NULL
        );
        """
        self.cursor.execute(query)
        self.conn.commit()
    
    def insert_data(self, data):
        for _, row in data.iterrows():
            query = """
            INSERT INTO SensorData (site_id, meter_id, timestamp, sensor_name, sensor_value, status)
            VALUES (?, ?, ?, ?, ?, ?)
            """
            self.cursor.execute(query, tuple(row))
        self.conn.commit()
    
    def close_connection(self):
        self.conn.close()
