FROM debian:bookworm-slim

# Install curl + certs (for fetching uv & Python)
RUN apt-get update && apt-get install -y curl ca-certificates \
 && rm -rf /var/lib/apt/lists/*

# Install uv
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.local/bin:$PATH"

# Let uv manage Python to match pyproject.toml
ENV UV_MANAGED_PYTHON=1

WORKDIR /app
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev

COPY . .
ENTRYPOINT ["uv", "run", "main.py"]
