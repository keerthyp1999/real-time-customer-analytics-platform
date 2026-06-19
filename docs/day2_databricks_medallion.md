# Day 2 - Databricks Medallion Architecture

## Objective

Build a Delta Lake medallion architecture using Databricks.

```text
Raw JSON → Bronze Delta → Silver Delta → Gold Delta
```

## Bronze Layer

Bronze stores source data with minimal transformation.

Added columns:

```text
ingestion_timestamp
```

Streaming trigger used:

```python
.trigger(availableNow=True)
```

This was used because the current cluster does not support infinite streaming triggers.

## Silver Layer

Silver applies quality and cleaning rules:

- Drop duplicate `event_id`
- Remove records with null `event_id`
- Remove records with null `user_id`
- Keep only valid event types
- Convert `event_time` to `event_timestamp`
- Add `silver_processed_timestamp`

## Gold Layer

Gold produces business metrics:

- Daily revenue
- User activity
- Event funnel
- Failed payments

## Key Learning

Databricks is used as the compute and Delta Lake storage layer. The medallion architecture separates raw ingestion, trusted cleaned data, and business-facing analytics tables.
