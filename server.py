from datetime import datetime
from fastapi import FastAPI
from pydantic import BaseModel

# 1. Create an instance of the FastAPI class (our main application object)
app = FastAPI()


class EventMessage(BaseModel):
    eventType: str
    categoryId: int
    categoryName: str
    timestamp: datetime


class UserEvent(BaseModel):
    topic: str
    message: EventMessage


# 2. Define an endpoint for the root URL ("/")
@app.get("/")
async def read_root():
    # 3. Return a simple JSON response
    return {"message": "Welcome to the Agentic AI SDK!"}


@app.post("/api/v1/user-events")
async def process_user_event(var: UserEvent):
    print(f"Received event for topic '{var.topic}'")
    print(f"     - Event Type '{var.message.eventType}'")
    print(f"     - Category '{var.message.categoryName}'")
    return {"status": "success", "event_received": var.message.eventType}
