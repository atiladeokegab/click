FROM python:3.10-slim

# Set work directory
WORKDIR /app

# Install curl and bash
RUN apt-get update \
 && apt-get install -y curl bash \
 && rm -rf /var/lib/apt/lists/*

# Install uv and update PATH
RUN curl -LsSf https://astral.sh/uv/install.sh | bash \
 && echo 'export PATH="/root/.local/bin:$PATH"' >> /root/.bashrc

# Set the PATH to include uv's install location
ENV PATH="/root/.local/bin:$PATH"

# Copy dependency files
COPY pyproject.toml uv.lock ./

# Install dependencies using uv
RUN uv sync

# Copy the rest of the source code
COPY . .

# Run the CLI by default
ENTRYPOINT ["python", "main.py"]
