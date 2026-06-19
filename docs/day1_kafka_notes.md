# Day 1 Kafka Notes

## What is Kafka?

Kafka is a distributed event streaming platform. It is used to move high-volume real-time data from producers to consumers.

## Producer

A producer writes messages to Kafka topics.

In this project:

```text
producer.py → customer_events topic
```

## Topic

A topic is a named stream of events.

In this project:

```text
customer_events
```

## Partition

A topic is split into partitions for scalability.

We use 3 partitions locally:

```text
Partition 0
Partition 1
Partition 2
```

## Message Key

The message key decides which partition receives the event.

In this project:

```text
key = user_id
```

This keeps events for the same user in order.

## Consumer

A consumer reads events from a Kafka topic.

In this project:

```text
test_consumer.py
```

## Consumer Group

A consumer group allows multiple consumers to share work.

Example:

```text
3 partitions + 3 consumers = parallel processing
```

## Offset

Offset is the position of a message inside a partition.

Kafka tracks offsets so consumers know where to continue reading.

## Reliability Concepts

This project uses:

```text
acks=all
retries=3
consumer group
offset tracking
partitioning by user_id
```

In production, you would also add:

```text
replication factor 3
schema registry
dead-letter queue
monitoring
manual offset commits
```
