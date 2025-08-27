import os, json
from kafka import KafkaProducer, KafkaConsumer


BROKERS = os.getenv("KAFKA_BROKERS", "localhost:29092").split(",")
CLIENT_ID = os.getenv("KAFKA_CLIENT_ID", "agentic-ai-sdk")

def get_consumer(group_id: str, topics: list[str]):
    return KafkaConsumer(
        *topics,
        bootstrap_servers=BROKERS,
        client_id=CLIENT_ID,
        group_id=group_id,
        auto_offset_reset="latest",
        enable_auto_commit=True,
        value_deserializer=lambda v: json.loads(v.decode("utf-8")),
    )

def get_producer():
    return KafkaProducer(
        bootstrap_servers=BROKERS,
        client_id=CLIENT_ID,
        key_serializer=lambda k: (str(k).encode() if k is not None else None),
        value_serializer=lambda v: json.dumps(v).encode(),
    )
