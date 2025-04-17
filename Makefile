dev:
	fastmcp dev server.py
run:
	fastmcp run server.py
run-sse:
	fastmcp run --transport sse --port 3001 server.py
test:
	uv run python test.py