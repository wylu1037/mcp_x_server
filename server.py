import os
from fastmcp import FastMCP
from agents.tweet_agent import agent

mcp = FastMCP("X MCP 🚀", description="A simple MCP server")

@mcp.tool()
def create_tweet(text: str) -> str:
    """Create a tweet"""
    return agent.run(text)

@mcp.tool()
def view_env():
    """View the environment variables"""
    return os.environ

if __name__ == "__main__":
    mcp.run(transport="stdio")