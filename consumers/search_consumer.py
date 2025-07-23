import json
from lib.kafka_client import get_kafka_consumer
from agents.task_manager import process_search_query # Assuming this function exists

def start_search_consumer():
    """
    Initializes and runs the Kafka consumer for user search events.
    This function runs in an infinite loop.
    """
    # This consumer subscribes to search events from ALL apps
    consumer = get_kafka_consumer(
        group_id='search-agent-group',
        topics=['dev.amazon-clone.user-searches', 'dev.swiggy-clone.restaurant-searches']
    )

    print("Search consumer started. Listening for user searches...")

    for message in consumer:
        try:
            # Topic format: {env}.{appName}.{eventType}
            app_name = message.topic.split('.')[1]
            payload = json.loads(message.value)

            print(f"[Search Consumer] Received event from app '{app_name}'")

            # Delegate the actual work to the agentic logic
            process_search_query(app_name, payload)

        except Exception as e:
            print(f"Error processing message: {e}")

