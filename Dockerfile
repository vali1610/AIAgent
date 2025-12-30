# Use Python 3.13 slim image
FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Install uv (fast Python package installer)
RUN pip install --no-cache-dir uv

# Copy project files
COPY . .

# Install dependencies using uv
RUN uv pip install --system -r requirements.txt || \
    uv pip install --system google-genai python-dotenv

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Default command - run the AI agent
ENTRYPOINT ["uv", "run", "main.py"]

# Default argument if none provided
CMD ["--help"]
