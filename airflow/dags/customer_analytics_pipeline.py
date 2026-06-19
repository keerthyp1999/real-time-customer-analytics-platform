"""
Airflow DAG for orchestrating the Customer Analytics medallion pipeline.

Current implementation uses PythonOperator placeholder tasks so the DAG structure
can be version-controlled and reviewed before integrating with Databricks Jobs API.

Production upgrade:
Replace PythonOperator tasks with DatabricksSubmitRunOperator tasks.
"""

from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator

# Production upgrade:
# from airflow.providers.databricks.operators.databricks import DatabricksSubmitRunOperator


DAG_ID = "customer_analytics_pipeline"
OWNER = "keerthy"


default_args = {
    "owner": OWNER,
    "depends_on_past": False,
    "retries": 2,
    "retry_delay": timedelta(minutes=5),
}


def generate_sample_events():
    """Placeholder for triggering Databricks notebook: 00_generate_sample_events."""
    print("Trigger Databricks notebook: 00_generate_sample_events")


def run_bronze_ingestion():
    """Placeholder for triggering Databricks notebook: 01_bronze_ingestion."""
    print("Trigger Databricks notebook: 01_bronze_ingestion")


def run_silver_transformations():
    """Placeholder for triggering Databricks notebook: 02_silver_transformations."""
    print("Trigger Databricks notebook: 02_silver_transformations")


def run_gold_aggregations():
    """Placeholder for triggering Databricks notebook: 03_gold_aggregations."""
    print("Trigger Databricks notebook: 03_gold_aggregations")


def validate_pipeline():
    """Placeholder validation task for Bronze, Silver, and Gold outputs."""
    print("Validate Bronze, Silver, and Gold output counts")


with DAG(
    dag_id=DAG_ID,
    default_args=default_args,
    description="Orchestrates customer analytics medallion pipeline",
    start_date=datetime(2026, 1, 1),
    schedule_interval="@daily",
    catchup=False,
    tags=["kafka", "databricks", "delta", "customer-analytics"],
) as dag:

    start = EmptyOperator(task_id="start")

    generate_events = PythonOperator(
        task_id="generate_sample_events",
        python_callable=generate_sample_events,
    )

    bronze_ingestion = PythonOperator(
        task_id="bronze_ingestion",
        python_callable=run_bronze_ingestion,
    )

    silver_transformations = PythonOperator(
        task_id="silver_transformations",
        python_callable=run_silver_transformations,
    )

    gold_aggregations = PythonOperator(
        task_id="gold_aggregations",
        python_callable=run_gold_aggregations,
    )

    validate = PythonOperator(
        task_id="validate_pipeline",
        python_callable=validate_pipeline,
    )

    end = EmptyOperator(task_id="end")

    start >> generate_events >> bronze_ingestion >> silver_transformations >> gold_aggregations >> validate >> end
