from pyspark.sql.functions import col, to_timestamp, current_timestamp, lit, when, concat_ws

BRONZE_PATH = "/Volumes/workspace/customer_analytics/data_files/bronze/customer_events"
SILVER_PATH = "/Volumes/workspace/customer_analytics/data_files/silver/customer_events"
QUARANTINE_PATH = "/Volumes/workspace/customer_analytics/data_files/silver/quarantine/customer_events"

valid_event_types = [
    "user_login",
    "product_view",
    "cart_add",
    "checkout",
    "payment_success",
    "payment_failed"
]

bronze_df = spark.read.format("delta").load(BRONZE_PATH)

staged_df = (
    bronze_df
    .withColumn("event_timestamp", to_timestamp(col("event_time")))
    .withColumn("silver_processed_timestamp", current_timestamp())
)

dq_df = (
    staged_df
    .withColumn(
        "dq_error_reason",
        concat_ws(
            ", ",
            when(col("event_id").isNull(), lit("event_id is null")),
            when(col("user_id").isNull(), lit("user_id is null")),
            when(~col("event_type").isin(valid_event_types), lit("invalid event_type")),
            when(col("event_timestamp").isNull(), lit("invalid event_time")),
            when(col("price") < 0, lit("negative price")),
            when(
                (col("event_type").isin(["payment_success", "payment_failed"])) & col("price").isNull(),
                lit("payment event missing price")
            )
        )
    )
)

valid_df = (
    dq_df
    .filter(col("dq_error_reason") == "")
    .dropDuplicates(["event_id"])
    .drop("dq_error_reason")
)

invalid_df = (
    dq_df
    .filter(col("dq_error_reason") != "")
)

valid_df.write.format("delta").mode("overwrite").save(SILVER_PATH)

invalid_df.write.format("delta").mode("overwrite").save(QUARANTINE_PATH)