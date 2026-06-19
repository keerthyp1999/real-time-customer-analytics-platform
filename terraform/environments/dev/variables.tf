variable "cluster_id" {
  description = "Existing Databricks cluster ID"
  type        = string
}

variable "bronze_notebook_path" {
  type    = string
  default = "/Users/your_email/customer-analytics/notebooks/bronze/01_bronze_ingestion"
}

variable "silver_notebook_path" {
  type    = string
  default = "/Users/your_email/customer-analytics/notebooks/silver/02_silver_transformations"
}

variable "gold_notebook_path" {
  type    = string
  default = "/Users/your_email/customer-analytics/notebooks/gold/03_gold_aggregations"
}