from .agent import run_recommendation_agent

if __name__ == "__main__":
    user_query = "Suggest a waterproof wireless speaker under ₹2000."
    result = run_recommendation_agent(user_query)
    print("\nAgent Recommendations:\n")
    print(result)

