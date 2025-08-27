from kafka import KafkaConsumer
import json

from langchain_ollama.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate


def consume_user_events():

    llm = ChatOllama(model="phi3:mini")

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are a user behavior analyst for an e-commerce platform. Your job is to interpret user events and provide a concise, one-sentence summary of the user's action.",
            ),
            ("human", "User event details: {event_data}"),
        ]
    )

    chain = prompt | llm

    eventsConsumer = KafkaConsumer(
        "dev.amazon-clone.user-events",
        bootstrap_servers=["localhost:29092"],
        group_id="events-agent-group-1",
        # This helps decode the message from bytes to a string
        value_deserializer=lambda m: json.loads(m.decode("utf-8")),
    )

    print("Consumer is listening for messages on 'dev.amazon-clone.user-events'...")

    # A consumer is like an iterable, we can loop over it forever
    for message in eventsConsumer:
        # message.value is the data we sent from our Next.js app
        print(f"Received message: {message.value}")

        response = chain.invoke({"event_data": message.value})
        print(f"AI Analysis: {response.content}")
