import json
from confluent_kafka import Consumer

consumer_config = {
    "bootstrap.servers": "localhost:9092",
    "group.id": "customer-activity-test-consumer",
    "auto.offset.reset": "earliest",
    "enable.auto.commit": True
}

consumer = Consumer(consumer_config)
consumer.subscribe(["customer_events"])

print("Listening to customer_events topic...")

try:
    while True:
        message = consumer.poll(1.0)

        if message is None:
            continue

        if message.error():
            print(f"Consumer error: {message.error()}")
            continue

        event = json.loads(message.value().decode("utf-8"))

        print(
            f"Consumed-2 | "
            f"user_id={event['user_id']} | "
            f"event_type={event['event_type']} | "
            f"partition={message.partition()} | "
            f"offset={message.offset()}"
        )

except KeyboardInterrupt:
    print("Stopping consumer...")

finally:
    consumer.close()
