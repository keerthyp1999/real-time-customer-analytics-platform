resource "databricks_job" "this" {

  name = var.job_name

  existing_cluster_id = var.cluster_id

  notebook_task {
    notebook_path = var.notebook_path
  }
}