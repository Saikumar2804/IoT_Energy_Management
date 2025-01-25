import pandas as pd

class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path
    
    def load_data(self):
        try:
            data = pd.read_csv(self.file_path)
            print("Data loaded successfully.")
            return data
        except Exception as e:
            print(f"Error loading data: {e}")
            return None
    
    def clean_data(self, data):
        # Drop rows with missing values
        data = data.dropna()
        # Remove invalid sensor_value readings
        data = data[data['sensor_value'] >= 0]
        print("Data cleaned successfully.")
        return data
