from kafka import KafkaProducer
import json
import time

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def create_user(username: str, email: str):
    event = {
        "event": "user_created",
        "username": username,
        "email": email,
        "timestamp": time.time()
    }
    print(f"[UserService] New user registered: {username}")
    producer.send("user_created", event)
    producer.flush()

  