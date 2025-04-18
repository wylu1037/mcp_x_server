FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

RUN if [ "$(uname -m)" = "aarch64" ]; then \
        curl -LsSf https://github.com/astral-sh/uv/releases/download/0.6.14/uv-aarch64-unknown-linux-gnu.tar.gz | tar xz -C /usr/local/bin --strip-components=1; \
    else \
        curl -LsSf https://github.com/astral-sh/uv/releases/download/0.6.14/uv-x86_64-unknown-linux-gnu.tar.gz | tar xz -C /usr/local/bin --strip-components=1; \
    fi

COPY . .

RUN uv pip compile pyproject.toml -o requirements.txt && \
    uv pip install --system --no-cache-dir -r requirements.txt

CMD ["python", "mcp_x_server/server.py"]