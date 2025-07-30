from fastapi import APIRouter
from pydantic import BaseModel
from langchain_orchestration.agent import run_recommendation_agent

router = APIRouter()

class RecommendationInput(BaseModel):
    user_query: str

@router.post("/recommend")
async def recommend_products(query: RecommendationInput):
    """
    Receives a user query and returns product recommendations.
    """
    result = run_recommendation_agent(query.user_query)
    return {"recommendations": result}
