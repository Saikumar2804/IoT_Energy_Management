from src.DataLoader import DataLoader
from src.DatabaseHandler import DatabaseHandler
from src.DataPreProcessor import DataPreProcessor
from src.MetricsCalculator import MetricsCalculator
from src.GraphGenerator import GraphGenerator
from src.DataReportGenerator import DataReportGenerator

def main():
    # Initialize components
    loader = DataLoader("data/IoT_Sensor_Data.csv")
    db_handler = DatabaseHandler("data/IoT_Sensor_Data.db")
    preprocessor = DataPreProcessor(db_handler)
    calculator = MetricsCalculator()
    grapher = GraphGenerator()
    reporter = DataReportGenerator()

    # Step 1: Load and clean data
    raw_data = loader.load_data()
    clean_data = loader.clean_data(raw_data)

    # Step 2: Insert data into database
    db_handler.create_table()
    db_handler.insert_data(clean_data)

    # Step 3: Process data
    query = "SELECT * FROM SensorData"
    data = preprocessor.fetch_data(query)
    normalized_data = preprocessor.normalize_data(data)

    # Step 4: Calculate metrics
    metrics = calculator.calculate_metrics(normalized_data)

    # Step 5: Generate filtered plot
    grapher.generate_filtered_plot(
        normalized_data,
        output_path="data/visualizations/Site_A_power_consumption.png",
        site_id="Site_A",
        sensor_name="power_consumption"
    )

    # Step 6: Export report
    reporter.export_to_csv(metrics, "data/output.csv")

    # Close database connection
    db_handler.close_connection()

if __name__ == "__main__":
    main()
