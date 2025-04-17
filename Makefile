dev:
	fastmcp dev server.py
run:
	fastmcp run server.py
run-sse:
	fastmcp run --transport sse server.py
test:
	uv run python test.py