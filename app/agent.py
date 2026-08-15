import os

from google.adk.agents.llm_agent import LlmAgent
from .prompt import orchestrator_prompt

root_agent = LlmAgent(
    model=os.getenv("MODEL_NAME"),
    name='stock_analysis_orchestrator',
    description='Stock Analysis Orchestrator',
    instruction=orchestrator_prompt,
)
