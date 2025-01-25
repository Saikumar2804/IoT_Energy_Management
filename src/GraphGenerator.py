import os
import matplotlib.pyplot as plt
import pandas as pd

class GraphGenerator:
    def generate_filtered_plot(self, data, output_path, site_id=None, sensor_name=None):
        # Filter by site_id and sensor_name
        if site_id:
            data = data[data['site_id'] == site_id]
        if sensor_name:
            data = data[data['sensor_name'] == sensor_name]

        # Ensure timestamp is in datetime format
        data['timestamp'] = pd.to_datetime(data['timestamp'])
        data = data.set_index('timestamp')

        # Convert sensor_value to numeric and drop invalid entries
        data['sensor_value'] = pd.to_numeric(data['sensor_value'], errors='coerce')
        data = data.dropna(subset=['sensor_value'])

        # Select only numeric columns for aggregation
        numeric_data = data[['sensor_value']]

        # Resample to hourly averages
        aggregated_data = numeric_data.resample('h').mean()  # Use lowercase 'h'

        # Ensure output directory exists
        output_dir = os.path.dirname(output_path)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Plot the aggregated data
        plt.figure(figsize=(12, 6))
        plt.plot(aggregated_data.index, aggregated_data['sensor_value'], label=f'{sensor_name} at {site_id}', color='blue')
        plt.title(f'{sensor_name} Over Time (Hourly Average)')
        plt.xlabel('Timestamp')
        plt.ylabel('Sensor Value (Normalized)')
        plt.legend()
        plt.grid(True)

        # Save the plot
        plt.savefig(output_path)
        plt.close()
        print(f"Filtered plot saved to {output_path}.")
