from langchain_community.llms import Ollama
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from .config import MODEL_NAME

# Connect to Ollama and set up an LLMChain
llm = Ollama(model=MODEL_NAME)

product_prompt = PromptTemplate(
    input_variables=["user_query"],
    template="""
You are an intelligent product assistant. Suggest 3 good e-commerce products with reasons.

User query: {user_query}
"""
)

recommendation_chain = LLMChain(llm=llm, prompt=product_prompt)

def run_recommendation_agent(user_query: str):
    return recommendation_chain.run(user_query)



