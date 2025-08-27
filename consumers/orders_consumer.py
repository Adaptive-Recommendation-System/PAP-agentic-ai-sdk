from consumers.kafka_io import get_consumer
import json

try:
    from langchain_ollama.chat_models import ChatOllama
    from langchain_core.prompts import ChatPromptTemplate

    llm = ChatOllama(model="phi3:mini")
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an order analyst. Summarize the order in one short sentence."),
        ("human", "Order event: {event_data}")
    ])
    chain = prompt | llm
except ImportError:
    chain = None


def validate_order(order: dict) -> bool:
    required = ["orderId", "userId", "items", "total", "status", "createdAt"]
    for field in required:
        if field not in order:
            print(f"[orders] ❌ Missing field: {field}")
            return False
    return True


def consume_order_events():
    consumer = get_consumer("orders-agent-group-1", ["dev.amazon-clone.orders"])
    print("[orders] Listening for events...")

    for msg in consumer:
        order = msg.value
        if isinstance(order, str):
            try:
                order = json.loads(order)
            except Exception:
                print("[orders] ⚠️ Could not parse message:", order)
                continue

        if not validate_order(order):
            continue

        print(f"[orders] ✅ orderId={order['orderId']} status={order['status']} total={order['total']}")

        if chain:
            try:
                summary = chain.invoke({"event_data": order})
                print("[orders] 🤖 AI Summary:", summary.content)
            except Exception as e:
                print("[orders] AI analysis failed:", e)

        # TODO: persist to DB or call another service


if __name__ == "__main__":
    consume_order_events()
