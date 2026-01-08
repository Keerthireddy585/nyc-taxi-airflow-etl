# nyc-taxi-airflow-etl
This project implements an end-to-end ETL pipeline using Apache Airflow (Dockerized) to process large-scale NYC Yellow Taxi trip data
The pipeline extracts raw data, performs memory-efficient transformations, and prepares clean, analytics-ready data for dashboarding and insights.


## Project Overview

The NYC Taxi ETL Pipeline is designed to demonstrate real-world data engineering practices such as:

- Workflow orchestration with Apache Airflow
- Handling large datasets efficiently using chunk-based processing
- Running data pipelines in a Dockerized environment
- Preparing data for analytics and visualization

The project focuses on robustness, scalability, and correctness, similar to production-grade ETL pipelines.


## Features

- End-to-end ETL pipeline (Extract -> Transform -> Load)
- Dockerized Apache Airflow setup
- Memory-efficient transformation of large CSV files
- Chunk-based processing to avoid Out-Of-Memory (OOM) errors
- Task dependency management and retries using Airflow
- Analytics-ready output for dashboards
- Clear logging and error handling


## Tools & Technologies

- **Apache Airflow** - Workflow orchestration
- **Docker & Docker Compose** - Containerized execution environment
- **Python** - ETL pipeline logic
- **Pandas** - Data transformation and processing
- **CSV Dataset** - NYC Yellow Taxi trip records
- **Power BI / Tableau** - Dashboarding & data visualization


## Prerequisites

Before running this project, ensure you have:
- Docker installed
-	Docker Compose installed
-	Basic knowledge of:
-	Python
-	Apache Airflow
-	Docker
-	Minimum 8 GB RAM recommended (chunking allows lower memory too)


## Setup Instructions


### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/nyc-airflow-etl.git
cd nyc-airflow-etl
```

### Step 2: Place Dataset

```text
dags/yellow_tripdata_2016-01.csv
```


## Running the Application

### Start Airflow using Docker Compose

```bash
docker compose up -d
```

### Restart Airflow (if DAG or data changes)

```bash
docker compose restart
```

### Access Airflow UI

http://localhost:8080
(Default credentials depend on your setup, usually airflow / airflow)

From the Airflow UI, you can:
- View and monitor DAG runs
- Check task execution status
- Inspect logs for each task
- Trigger workflows manually
- Clear failed or retry tasks


## How the Pipeline Works

### Extract Data
-	Reads the raw NYC Taxi CSV file from Airflow’s DAGs directory.
-	Validates file availability.

### Transform Data
-	Reads data in small chunks using Pandas.
-	Cleans data (e.g., removes null values).
-	Writes transformed data incrementally to avoid memory overload.

### Load Data
-	Reads the cleaned dataset.
-	Verifies row count and schema.
-	Makes data ready for analytics and dashboards.


## Handling Errors & Logs
Airflow logs are available for each task via the UI.

Logs include:
-	Task execution state
-	Errors and stack traces
-	Retry attempts
-	Chunk-based processing prevents memory-related crashes 


## Troubleshooting
- **Airflow UI not accessible at `http:\\localhost:8080`**
Check running containers using `docker compose ps`.  
If required, restart Airflow services.
- **Task fails with FileNotFoundError**
Ensure the dataset is placed inside the `dags/` directory and that the file path used in the DAG matches the actual file location.
- **Out-Of-Memory (OOM) error during transformation**
This can occur when processing large CSV files.
The pipeline uses chunk-based processing to reduce memory usage. Ensure chunking logic is enabled in the transform task.
- **Downstream tasks marked as Upstream Failed**
This indicates a failure in a previous task.
Clear the failed task and rerun the DAG from the Airflow UI.


## Testing
- Verified DAG execution through Airflow UI
- Confirmed successful completion of:
- extract_data
- transform_data
- load_data
- Validated output CSV file size and row count

## Dashboard & Analytics
The cleaned dataset is used to build an interactive dashboard with insights such as: 
-	Total trips
-	Trips by hour/day
-	Average trip distance
-	Fare distribution
-	Peak demand periods

**Tools Used**: Power BI


## Dependancies & Commands Used

### Python Dependancies

```text
pandas
apache-airflow
apache-airflow-providers-standard
```

### Docker Commands Used

```bash
docker compose up -d
docker compose restart
docker ps
docker exec -it <container_name> bash
```

### Airflow Operations
- Clear only failed tasks
- View logs per task
- Manual DAG trigger
- Task retries and dependency handling

## Conclusion & Future Enhancements
This project demonstrates a production-style data engineering pipeline with **Airflow** and **Docker**.
It highlights best practices for handling large datasets, task orchestration, and analytics preparation.

### Future Enhancements:
- Enable fully automated scheduled DAG runs for continuous data ingestion
- Parameterize DAG for multiple months / datasets
- Add data quality checks and validation tasks
- Store processed data in a database or data warehouse
- Add alerting (email / Slack) on task failures
- Extend dashboards with additional KPIs and filters









































