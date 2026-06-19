# Airflow Orchestration

This folder contains the Airflow DAG for orchestrating the customer analytics medallion pipeline.

## DAG

```text
dags/customer_analytics_pipeline.py
```

## Current Flow

```text
start
  ↓
generate_sample_events
  ↓
bronze_ingestion
  ↓
silver_transformations
  ↓
gold_aggregations
  ↓
validate_pipeline
  ↓
end
```

## Current Implementation

The DAG currently uses `PythonOperator` placeholder tasks. This keeps the project runnable and easy to understand locally.

## Production Upgrade

In production, replace the PythonOperator placeholders with:

```python
DatabricksSubmitRunOperator
```

This allows Airflow to trigger Databricks notebooks using the Databricks Jobs API.

Terraform provisions Bronze, Silver, and Gold Databricks jobs.
Airflow orchestrates those jobs in dependency order.

## Reliability Features Included

- Retry configuration
- Retry delay
- Explicit task dependencies
- Catchup disabled
- Validation task placeholder
