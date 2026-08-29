import os

from google.adk.tools.mcp_tool.mcp_toolset import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from mcp import StdioServerParameters

tavily_internet_search = McpToolset(
    connection_params=StdioConnectionParams(
        server_params=StdioServerParameters(
            command="npx",
            args=["-y", "tavily-mcp@latest"],
            env={"TAVILY_API_KEY": os.getenv("TAVILY_API_KEY")}
        ),
        timeout=60
    )
)