import os

from google.adk.agents.llm_agent import LlmAgent
from app.tools.tavily_internet_seach import tavily_internet_search
from .prompt import NEWS_ANALYSIS_PROMPT

news_analysis_agent = LlmAgent(
    model=os.getenv("MODEL_NAME"),
    name="news_analysis_agent",
    description="An agent that can provide a summary of current news and events surrounding a company.",
    instruction=NEWS_ANALYSIS_PROMPT,
    tools=[tavily_internet_search],
)