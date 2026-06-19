# Day 3 - Airflow Notes

## What Airflow Does

Airflow orchestrates tasks. It does not process large data itself.

In this project, Airflow controls the execution order:

```text
Generate Events → Bronze → Silver → Gold → Validate
```

## Important Concepts

### DAG

A DAG is a pipeline definition with ordered tasks.

### Operator

An operator defines the type of work a task performs.

Current project operator:

```python
PythonOperator
```

Production operator planned:

```python
DatabricksSubmitRunOperator
```

### Task Dependency

```python
start >> bronze >> silver >> gold
```

means each task runs only after the previous task succeeds.

## Production Pattern

In production:

```text
Airflow → Databricks Jobs API → Databricks Notebook → Spark Cluster
```

Airflow tracks status, retries failed tasks, and provides logs.
