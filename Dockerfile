FROM ghcr.io/astral-sh/uv:python3.13-bookworm

WORKDIR /app
# No managed Python needed; it’s already there
COPY pyproject.toml uv.lock ./
RUN uv sync

COPY . .
ENTRYPOINT ["uv", "run", "main.py"]
