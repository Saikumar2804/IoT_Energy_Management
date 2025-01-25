import pandas as pd
import numpy as np

class DataPreProcessor:
    def __init__(self, db_handler):
        self.db_handler = db_handler
    
    def fetch_data(self, query):
        return pd.read_sql_query(query, self.db_handler.conn)
    
    def normalize_data(self, data):
        data['sensor_value'] = (data['sensor_value'] - data['sensor_value'].min()) / (data['sensor_value'].max() - data['sensor_value'].min())
        print("Data normalized successfully.")
        return data
    
    def fill_missing_timestamps(self, data):
        data['timestamp'] = pd.to_datetime(data['timestamp'])
        data = data.set_index('timestamp').asfreq('5T')
        data = data.interpolate()
        print("Missing timestamps filled successfully.")
        return data
