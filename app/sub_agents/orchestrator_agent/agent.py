from google.adk.agents import LoopAgent
from app.sub_agents.research_agent.agent import research_agent
from app.sub_agents.checker_agent.agent import checker_agent

orchestrator_agent = LoopAgent(
    name='orchestrator_agent',
    description='Agent that orchestrates the stock analysis process.',
    sub_agents=[
        research_agent,
        checker_agent
    ],
    max_iterations=10, 
)