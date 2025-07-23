from kafka import KafkaProducer, KafkaConsumer

KAFKA_BROKER_URL = 'localhost:29092'
CLIENT_ID = 'agentic-ai-sdk'

def get_kafka_consumer(group_id: str, topics: list[str]):
    """Creates and returns a Kafka consumer."""
    return KafkaConsumer(
        *topics,
        bootstrap_servers=KAFKA_BROKER_URL,
        client_id=CLIENT_ID,
        group_id=group_id,
        auto_offset_reset='earliest',
        value_deserializer=lambda v: v.decode('utf-8')
    )

def get_kafka_producer():
    """Creates and returns a Kafka producer."""
    return KafkaProducer(
        bootstrap_servers=KAFKA_BROKER_URL,
        client_id=CLIENT_ID,
        value_serializer=lambda v: v.encode('utf-8')
    )
