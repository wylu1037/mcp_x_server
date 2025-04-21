# MCP X Server
What can you do with MCP X Server? Give it a sentence or a topic, and it will help you write and refine a tweet, then publish it to X.

## How to run with STDIO

### Local
Configure the MCP server in mcp.json.
```json
{
    "mcpServices": {
        "x-mcp": {
            "command": "uv",
            "args": [
                "run",
                "--with",
                "fastmcp",
                "--with",
                "pydantic-ai",
                "--with",
                "pydantic-ai-slim[duckduckgo,openai]",
                "--with",
                "dotenv",
                "--with",
                "python-twitter-v2",
                "fastmcp",
                "run",
                "mcp_x_server/server.py"
            ],
            "env": {
                "CONSUMER_KEY": "*******************",
                "CONSUMER_SECRET": "*******************",
                "ACCESS_TOKEN": "*******************",
                "ACCESS_SECRET": "*******************",
                "DEEPSEEK_API_KEY": "*******************"
            }
        }
    }
}
```

### Docker
Configure the MCP server in mcp.json.
```json
{
    "mcpServices": {
        "x-mcp-docker": {
        "command": "docker",
        "args": [
          "run",
          "-i",
          "--rm",
          "--name",
          "mcp-x-server",
          "-e",
          "CONSUMER_KEY",
          "-e",
          "CONSUMER_SECRET",
          "-e",
          "ACCESS_TOKEN",
          "-e",
          "ACCESS_SECRET",
          "-e",
          "DEEPSEEK_API_KEY",
          "wylu1037/mcp-x-server:latest"
        ],
        "env": {
          "CONSUMER_KEY": "********************************",
          "CONSUMER_SECRET": "********************************",
          "ACCESS_TOKEN": "********************************",
          "ACCESS_SECRET": "********************************",
          "DEEPSEEK_API_KEY": "sk-********************************"
        }
      }
    }
}
```

### UVX
Configure the MCP server in mcp.json.
```json
{
    "mcpServices": {
        "mcp-x-server": {
        "command": "uvx",
        "args": [
          "mcp-x-server"
        ],
        "env": {
          "CONSUMER_KEY": "********************************",
          "CONSUMER_SECRET": "********************************",
          "ACCESS_TOKEN": "********************************",
          "ACCESS_SECRET": "********************************",
          "DEEPSEEK_API_KEY": "sk-********************************"
        }
      }
    }
}
```

## Run with SSE
Run MCP server
```shell
fastmcp run --transport sse mcp_x_server/server.py
```

Configure the MCP server in mcp.json.
```json
{
    "mcpServices": {
        "mcp-x-server": {
            "url": "http://localhost:8000/sse"
        }
    }
}
```
