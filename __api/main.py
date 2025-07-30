from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from __api.endpoints import router

app = FastAPI(title="Product Recommendation API")

# Add CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],         # Allows all origins; consider specifying domains for production
    allow_credentials=True,
    allow_methods=["*"],         # Allow all HTTP methods (GET, POST, etc)
    allow_headers=["*"],         
)

app.include_router(router, prefix="/agent", tags=["ProductAgent"])
