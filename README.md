# IoT Energy Management Project

## Overview
This project is designed to analyze IoT sensor data from multiple sites to provide actionable insights for energy management. It includes data cleaning, processing, metrics calculation, and visualization. The solution is containerized using Docker for easy deployment.

---

## Features
- **Data Cleaning**: Handles missing or invalid data values.
- **SQL Queries**: Extracts insights like power consumption and missing timestamps.
- **Data Aggregation**: Resamples data into hourly averages.
- **Visualization**: Generates time-series plots for different sites and sensors.
- **Dockerized Solution**: Runs the entire pipeline inside a container.

---

## Project Structure
```
IoT_Project/
├── src/                       # Source code directory
│   ├── DataLoader.py          # Handles data loading and cleaning
│   ├── DatabaseHandler.py     # Manages SQLite database operations
│   ├── DataPreProcessor.py    # Normalizes and aggregates data
│   ├── MetricsCalculator.py   # Calculates metrics like averages and sums
│   ├── GraphGenerator.py      # Generates visualizations
│   ├── DataReportGenerator.py # Exports metrics to CSV
├── data/                      # Input/output directory
│   ├── IoT_Sensor_Data.csv    # Input data
│   ├── output.csv             # Metrics report
│   ├── visualizations/        # Folder for PNG plots
├── requirements.txt           # Python dependencies
├── Dockerfile                 # Docker configuration file
├── README.md                  # Project documentation
└── main.py                    # Main script to orchestrate the pipeline
```

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <repository_url>
cd IoT_Project
```

### 2. Install Python Dependencies (Optional)
If running locally without Docker:
```bash
pip install -r requirements.txt
```

### 3. Build the Docker Image
```bash
docker build -t iot_project .
```

### 4. Run the Docker Container
Run the container and mount the `data` directory for input and output:
```bash
docker run --rm -v C:\Users\saiku\IoT_Project\data:/app/data iot_project
```

---

## Steps Taken

### Data Cleaning
1. **Handling Missing Values**:
   - Dropped rows with missing `sensor_value`.
   - Converted `sensor_value` to numeric and removed invalid entries.
2. **Filtering**:
   - Focused on specific `site_id` and `sensor_name` to reduce clutter.
3. **Timestamp Conversion**:
   - Converted `timestamp` column to datetime for proper time-series operations.

### SQL Queries and Purpose
1. **Total Power Consumption**:
   - Calculates the total power usage for each site.
   ```sql
   SELECT site_id, SUM(sensor_value) AS total_power 
   FROM SensorData
   WHERE sensor_name = 'power_consumption'
   GROUP BY site_id;
   ```
2. **Meters with Highest Power Usage**:
   - Identifies meters contributing the most power consumption at each site.
   ```sql
   SELECT site_id, meter_id, SUM(sensor_value) AS total_power 
   FROM SensorData
   WHERE sensor_name = 'power_consumption'
   GROUP BY site_id, meter_id
   ORDER BY total_power DESC;
   ```
3. **Missing Timestamps**:
   - Finds gaps in the time-series data.
   ```sql
   SELECT site_id, meter_id, timestamp 
   FROM SensorData
   WHERE status = 'error';
   ```

### Challenges and Resolutions
1. **Challenge**: Handling large datasets with missing or invalid values.
   - **Resolution**: Used Pandas to clean and preprocess the data.
2. **Challenge**: Overlapping plots due to dense time-series data.
   - **Resolution**: Resampled data to hourly averages.
3. **Challenge**: Docker build errors for dependencies.
   - **Resolution**: Removed unnecessary packages (`sqlite3`) from `requirements.txt` and upgraded `pip` during the build process.

---

## Outputs
1. **Plots**:
   - Saved in `data/visualizations/` as PNG files.
   - Example: `Site_A_power_consumption.png`.
2. **Metrics Report**:
   - Exported to `data/output.csv`.

---

## Run Commands Summary
1. **Build the Docker Image**:
   ```bash
   docker build -t iot_project .
   ```
2. **Run the Docker Container**:
   ```bash
   docker run --rm -v C:\Users\saiku\IoT_Project\data:/app/data iot_project
