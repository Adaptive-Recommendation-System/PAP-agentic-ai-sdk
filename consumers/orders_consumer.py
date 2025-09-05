from kafka import KafkaConsumer
import json

from langchain_ollama.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate


def consume_orders_events():

    llm = ChatOllama(model="phi3:mini")

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are an order analyst for an e-commerce platform. Your job is to interpret order details and provide a concise, one-sentence summary of the order.",
            ),
            ("human", "Order event: {event_data}"),
        ]
    )

    chain = prompt | llm

    ordersConsumer = KafkaConsumer(
        "dev.amazon-clone.orders",
        bootstrap_servers=["localhost:29092"],
        group_id="events-agent-group-2",
        # This helps decode the message from bytes to a string
        value_deserializer=lambda m: json.loads(m.decode("utf-8")),
    )

    print("Consumer is listening for messages on 'dev.amazon-clone.orders'...")

    # A consumer is like an iterable, we can loop over it forever
    for message in ordersConsumer:
        # message.value is the data we sent from our Next.js app
        print(f"Received message: {message.value}")

        response = chain.invoke({"event_data": message.value})
        print(f"AI Analysis: {response.content}")
