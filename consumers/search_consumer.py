from kafka import KafkaConsumer
import json


def consume_search_events():
    searchConsumer = KafkaConsumer(
        "dev.amazon-clone.user-searches",
        bootstrap_servers=["localhost:29092"],
        group_id="search-agent-group-1",
        # This helps decode the message from bytes to a string
        value_deserializer=lambda m: json.loads(m.decode("utf-8")),
    )

    print("Consumer is listening for messages on 'dev.amazon-clone.user-searches'...")

    # A consumer is like an iterable, we can loop over it forever
    for message in searchConsumer:
        # message.value is the data we sent from our Next.js app
        print(f"Received message: {message.value}")
