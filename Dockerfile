FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y curl && \
    pip install uv

COPY . .

RUN uv pip compile pyproject.toml -o requirements.txt && \
    uv pip install --system --no-cache-dir -r requirements.txt

CMD ["python", "server.py"]
