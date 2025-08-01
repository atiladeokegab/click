FROM python:3.10-slim

WORKDIR /app

# Install curl and bash
RUN apt-get update \
 && apt-get install -y curl bash \
 && rm -rf /var/lib/apt/lists/*

# Install uv
RUN curl -LsSf https://astral.sh/uv/install.sh | bash



# Add uv to PATH
ENV PATH="/root/.local/bin:$PATH"

# Prevent uv from downloading Python unless necessary
ENV UV_NO_PYTHON_DOWNLOADS=1

# Copy dependency files first
COPY pyproject.toml uv.lock ./

# Create virtualenv and install deps inside it
RUN uv sync

# Copy the rest of the app
COPY . .

# ✅ Use venv's Python interpreter explicitly
ENTRYPOINT ["uv", "run", "main.py"]

