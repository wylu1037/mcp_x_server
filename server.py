from fastmcp import FastMCP
from agents.tweet_agent import agent

mcp = FastMCP("X MCP 🚀", description="A simple MCP server")

@mcp.tool()
def create_tweet(text: str) -> str:
    """Create a tweet"""
    # Ignore the return value
    agent.run(text) 
    return "Tweet created successfully"

if __name__ == "__main__":
    mcp.run(transport="stdio")