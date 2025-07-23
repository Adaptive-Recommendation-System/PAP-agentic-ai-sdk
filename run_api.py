import uvicorn

if __name__ == "__main__":
    """
    This script starts the FastAPI application using Uvicorn.
    It's the entry point for our API service container.
    """
    uvicorn.run("api.main:app", host="0.0.0.0", port=8000, reload=True)
