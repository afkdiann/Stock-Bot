import os 

from google.adk.agents import ParallelAgent
from app.sub_agents.fundamentals_agent.agent import fundamentals_agent
from app.sub_agents.news_analysis_agent.agent import news_analysis_agent
from app.sub_agents.public_sentiments_agent.agent import public_sentiments_agent

research_agent = ParallelAgent(
    name="research_agent",
    description="An agent with access to the internet to do general research on investments",
    sub_agents=[
        fundamentals_agent,
        news_analysis_agent,
        public_sentiments_agent,
    ],
)