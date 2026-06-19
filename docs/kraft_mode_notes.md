# Kafka KRaft Mode Notes

Earlier Kafka used ZooKeeper for cluster coordination and metadata management.

Modern Kafka can run in KRaft mode, which means Kafka manages metadata internally without ZooKeeper.

## Old Setup

```text
Kafka Broker + ZooKeeper
```

## New Setup

```text
Kafka Broker + Kafka Controller
```

In this local project, the same Kafka container acts as both:

```text
broker,controller
```

## Why KRaft is better

```text
No ZooKeeper dependency
Cleaner local setup
Modern Kafka architecture
Easier to explain in interviews
Closer to current Kafka direction
```

## Production note

In real production, you would not use only one node.

A production KRaft setup usually has:

```text
3 or 5 controller nodes
multiple broker nodes
replication factor 3
monitoring
security
```
