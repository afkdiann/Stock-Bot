import os

from google.adk.agents.llm_agent import LlmAgent
from app.tools.tavily_internet_seach import tavily_internet_search
from .prompt import PUBLIC_SENTIMENTS_PROMPT

public_sentiments_agent = LlmAgent(
    model=os.getenv("MODEL_NAME"),
    name="public_sentiments_agent",
    description="An agent that can provide a summary of current public sentiments surrounding a company.",
    instruction=PUBLIC_SENTIMENTS_PROMPT,
    tools=[tavily_internet_search],
)