import asyncio

from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from google.genai import types
from app.agent import root_agent
from app.sub_agents.fundamentals_agent.agent import fundamentals_agent

session_service = InMemorySessionService()

APP_NAME = "Stock Bot"
USER_ID = "dev123"

async def main():
    session = await session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID
    )
    SESSION_ID = session.id

    runner = Runner(
        agent=fundamentals_agent,
        app_name=APP_NAME,
        session_service=session_service
    )

    content = types.Content(
        role='user', parts=[types.Part(text="What is the current price of Apple stock? (AAPL)")]
    )

    async for event in runner.run_async(
        user_id=USER_ID,
        session_id=SESSION_ID,
        new_message=content
    ):
        if event.is_final_response():
            if event.content and event.content.parts:
                print(f"Final Response:\n{event.content.parts[0].text}")

if __name__ == "__main__":
    asyncio.run(main())