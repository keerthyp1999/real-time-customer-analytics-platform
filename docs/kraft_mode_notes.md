# Kafka KRaft Mode Notes

## What Changed?

Older Kafka versions used ZooKeeper for cluster coordination and metadata management.

Modern Kafka can run in KRaft mode, where Kafka manages metadata internally without ZooKeeper.

## Old Setup

```text
Kafka Broker + ZooKeeper
```

## New Setup

```text
Kafka Broker + Kafka Controller
```

## Local Project Setup

The same Kafka container acts as both broker and controller:

```text
KAFKA_PROCESS_ROLES=broker,controller
```

## Why KRaft is Better for This Project

- No ZooKeeper dependency
- Cleaner local setup
- Modern Kafka architecture
- Easier to explain in interviews

## Production Note

A real production KRaft setup usually has:

- Multiple broker nodes
- 3 or 5 controller nodes
- Replication factor 3
- Monitoring
- Security
- Proper storage and backup strategy
