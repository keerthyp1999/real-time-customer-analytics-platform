#!/bin/bash

docker exec kafka-kraft kafka-topics \
  --bootstrap-server localhost:9092 \
  --create \
  --if-not-exists \
  --topic customer_events \
  --partitions 3 \
  --replication-factor 1

docker exec kafka-kraft kafka-topics \
  --bootstrap-server localhost:9092 \
  --describe \
  --topic customer_events
