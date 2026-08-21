import os

from google.adk.agents.llm_agent import LlmAgent
from .prompt import ORCHESTRATOR_PROMPT

root_agent = LlmAgent(
    model=os.environ.get("MODEL_NAME"),
    name='stock_analysis_orchestrator',
    description='Stock Analysis Orchestrator',
    instruction=ORCHESTRATOR_PROMPT,
)
