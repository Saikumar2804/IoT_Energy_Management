class MetricsCalculator:
    def calculate_metrics(self, data):
        metrics = data.groupby('site_id').agg({
            'sensor_value': ['mean', 'max', 'sum']
        })
        metrics.columns = ['average', 'max', 'total']
        print("Metrics calculated successfully.")
        return metrics