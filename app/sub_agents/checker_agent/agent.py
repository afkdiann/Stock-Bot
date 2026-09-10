import os

from google.adk.agents.llm_agent import LlmAgent
from .prompt import CHECKER_AGENT_PROMPT

checker_agent = LlmAgent(
    model=os.getenv("MODEL_NAME"),
    name="checker_agent",
    description="An agent that checks and validates the output of another agent",
    instruction=CHECKER_AGENT_PROMPT,
)   