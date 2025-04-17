# MCP X Server

## Build image
```shell
docker build -t mcp-x-server:latest .
```

## How to run with STDIO
### Docker
```
docker run -i \
  -e CONSUMER_KEY="your-consumer-key" \
  -e CONSUMER_SECRET="your-consumer-secret" \
  -e ACCESS_TOKEN="your-access-token" \
  -e ACCESS_SECRET="your-access-secret" \
  -e DEEPSEEK_API_KEY="your-deepseek-key" \
  mcp-x-server:latest
```