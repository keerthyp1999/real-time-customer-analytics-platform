# Databricks Pipeline

This folder contains the Databricks notebooks used to implement the medallion architecture.

## Notebook Execution Order

```text
notebooks/bronze/00_generate_sample_events.ipynb
notebooks/bronze/01_bronze_ingestion.ipynb
notebooks/silver/02_silver_transformations.ipynb
notebooks/gold/03_gold_aggregations.ipynb
```

## Utility Notebook

```text
notebooks/utilities/config.ipynb
```

The config notebook contains shared paths and business rules used by the Bronze, Silver, and Gold notebooks.

## Unity Catalog Setup

Expected catalog/schema/volume:

```text
Catalog : workspace
Schema  : customer_analytics
Volume  : data_files
```

Expected storage path:

```text
/Volumes/workspace/customer_analytics/data_files/
```

Expected folders:

```text
raw/
bronze/
silver/
gold/
checkpoints/
```

## Layer Responsibilities

### Bronze

Raw ingestion layer. Reads JSON records from the raw path and writes them to Delta with ingestion metadata.

### Silver

Clean trusted layer. Applies deduplication, required-field checks, event type validation, and timestamp conversion.

### Gold

Business analytics layer. Creates revenue, user activity, funnel, and failed payment metrics.
