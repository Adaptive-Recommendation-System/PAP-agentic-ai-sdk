import threading
from consumers.events_consumer import consume_user_events
from consumers.search_consumer import consume_search_events

if __name__ == "__main__":
    print("Starting AI Agent consumers...")

    events_thread = threading.Thread(target=consume_user_events)
    search_thread = threading.Thread(target=consume_search_events)

    events_thread.start()
    search_thread.start()

    print("All consumers are running in the background.")

    events_thread.join()
    search_thread.join()

    print("Application has finished.")
