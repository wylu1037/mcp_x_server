dev:
	fastmcp dev mcp_x_server/server.py
run:
	fastmcp run mcp_x_server/server.py
run-sse:
	fastmcp run --transport sse mcp_x_server/server.py
test:
	uv run python test.py