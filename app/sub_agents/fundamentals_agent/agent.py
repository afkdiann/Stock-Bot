import os

from google.adk.agents.llm_agent import LlmAgent
from .prompt import FUNDAMENTALS_PROMPT

fundamentals_agent = LlmAgent(
    model=os.getenv("MODEL_NAME"),
    name="fundamentals_agent",
    description="An agent that can provide a summary of current fundamentals of a company.",
    instruction=FUNDAMENTALS_PROMPT
)