import random
import uuid
from datetime import datetime, timezone

from config import EVENT_TYPES, PRODUCT_CATEGORIES, PAYMENT_METHODS

def generate_customer_event() -> dict:
    event_type = random.choice(EVENT_TYPES)

    event = {
        "event_id": str(uuid.uuid4()),
        "user_id": f"U{random.randint(1000, 9999)}",
        "session_id": str(uuid.uuid4()),
        "event_type": event_type,
        "product_id": None,
        "category": None,
        "price": None,
        "quantity": None,
        "payment_method": None,
        "event_time": datetime.now(timezone.utc).isoformat(),
        "source": "web_app"
    }

    if event_type in ["product_view", "cart_add", "checkout", "payment_success", "payment_failed"]:
        event["product_id"] = f"P{random.randint(100, 999)}"
        event["category"] = random.choice(PRODUCT_CATEGORIES)
        event["price"] = round(random.uniform(10, 500), 2)
        event["quantity"] = random.randint(1, 5)

    if event_type in ["payment_success", "payment_failed"]:
        event["payment_method"] = random.choice(PAYMENT_METHODS)

    return event
