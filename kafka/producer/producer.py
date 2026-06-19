import json
import time
from confluent_kafka import Producer

from config import KAFKA_BOOTSTRAP_SERVERS, CUSTOMER_EVENTS_TOPIC
from event_generator import generate_customer_event

producer_config = {
    "bootstrap.servers": KAFKA_BOOTSTRAP_SERVERS,
    "client.id": "customer-activity-producer",
    "acks": "all",
    "retries": 3
}

producer = Producer(producer_config)

def delivery_report(error, message):
    if error is not None:
        print(f"Delivery failed: {error}")
    else:
        print(
            f"Event delivered | topic={message.topic()} "
            f"partition={message.partition()} offset={message.offset()}"
        )

def start_producer():
    print("Starting customer activity producer...")

    while True:
        event = generate_customer_event()
        message_key = event["user_id"]

        producer.produce(
            topic=CUSTOMER_EVENTS_TOPIC,
            key=message_key,
            value=json.dumps(event),
            callback=delivery_report
        )

        producer.poll(0)
        time.sleep(1)

if __name__ == "__main__":
    try:
        start_producer()
    except KeyboardInterrupt:
        print("Stopping producer...")
    finally:
        producer.flush()
