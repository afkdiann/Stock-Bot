import os 

from google.adk.agents.llm_agent import LlmAgent
from .prompt import RESEARCH_AGENT_PROMPT

research_agent = LlmAgent(
    model=os.getenv("MODEL_NAME"),
    name="research_agent",
    description="An agent with access to the internet to do general research on investments",
    instruction=RESEARCH_AGENT_PROMPT,
)