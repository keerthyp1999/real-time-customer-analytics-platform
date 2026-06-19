module "bronze_job" {
  source = "../../modules/databricks_job"

  job_name      = "customer-analytics-bronze-ingestion-dev"
  notebook_path = var.bronze_notebook_path
  cluster_id    = var.cluster_id
}

module "silver_job" {
  source = "../../modules/databricks_job"

  job_name      = "customer-analytics-silver-transformations-dev"
  notebook_path = var.silver_notebook_path
  cluster_id    = var.cluster_id
}

module "gold_job" {
  source = "../../modules/databricks_job"

  job_name      = "customer-analytics-gold-aggregations-dev"
  notebook_path = var.gold_notebook_path
  cluster_id    = var.cluster_id
}