import os

from google.adk.agents.llm_agent import LlmAgent
from google.adk.agents.callback_context import CallbackContext
from google.adk.tools.agent_tool import AgentTool
from google.adk.models import LlmRequest, LlmResponse
from google import genai
from google.genai import types
from .prompt import ORCHESTRATOR_PROMPT
from .sub_agents.fundamentals_agent.agent import fundamentals_agent
from .sub_agents.news_analysis_agent.agent import news_analysis_agent
from .sub_agents.public_sentiments_agent.agent import public_sentiments_agent

api_key = os.environ.get("GOOGLE_API_KEY")
client = genai.Client(api_key=api_key)

MODEL_NAME=os.environ.get("MODEL_NAME")

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    """
    Callback function to check if the user is asking you whether they should buy, sell, or hold a stock.

    Args:
        callback_context: contains state and context information
        llm_request: the LLM request being sent

    Returns:
        None if the request is not about buying, selling, or holding a stock
        LlmResponse if the request is about buying, selling, or holding a stock
    """
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=f"Check if the user is asking you whether they should buy, sell, or hold a stock. If it does, respond with 'true'. Otherwise, respond with 'false'. Here's the user's request: {llm_request}."
    )
    if 'true' in response.text:
        return LlmResponse(
            content=types.Content(
                role="model",
                parts=[types.Part(text="Your request could not be processed. You likely asked the agent whether you should buy, sell, or hold a stock.")]
            )
        )
    return None

def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    """
    Callback function to check if the LLM's response contains any suggestions to buy, sell, or hold a stock.

    Args:
        callback_context: contains state and context information
        llm_response: the LLM response to check

    Returns:
        None if the response is not about buying, selling, or holding a stock
        LlmResponse if the response is about buying, selling, or holding a stock
    """
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=f"Check if the LLM's response contains any suggestions to buy, sell, or hold a stock. If it does, respond with 'true'. Otherwise, respond with 'false'. Here's the LLM's response: {llm_response}"
    )
    if 'true' in response.text:
        return LlmResponse(
            content=types.Content(
                role="model",
                parts=[types.Part(text="Your request could not be processed. Please try again.")]
            )
        )
    return None

root_agent = LlmAgent(
    model=MODEL_NAME,
    name='stock_analysis_orchestrator',
    description='Stock Analysis Orchestrator',
    instruction=ORCHESTRATOR_PROMPT,
    tools=[
        AgentTool(agent=fundamentals_agent),
        AgentTool(agent=news_analysis_agent),
        AgentTool(agent=public_sentiments_agent),
    ],
    before_model_callback=before_model_callback,
    after_model_callback=after_model_callback
)
