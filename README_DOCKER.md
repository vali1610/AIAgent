# AI Agent - Docker Setup

## Quick Start

### 1. Build the Docker image
```bash
docker build -t aiagent:latest .
```

### 2. Run with Docker
```bash
# Make sure your GEMINI_API_KEY is set in .env file
docker run --rm \
  --env-file .env \
  -v $(pwd)/calculator:/app/calculator \
  aiagent:latest "how does the calculator work?"
```

### 3. Run with Docker Compose
```bash
# Make sure GEMINI_API_KEY is in .env
docker-compose up
```

## Usage Examples

### Ask about code
```bash
docker run --rm --env-file .env -v $(pwd)/calculator:/app/calculator \
  aiagent:latest "explain how the calculator renders results"
```

### Run tests
```bash
docker run --rm --env-file .env -v $(pwd)/calculator:/app/calculator \
  aiagent:latest "run the calculator tests"
```

### List files
```bash
docker run --rm --env-file .env -v $(pwd)/calculator:/app/calculator \
  aiagent:latest "what files are in the root directory?"
```

### Create new files
```bash
docker run --rm --env-file .env -v $(pwd)/calculator:/app/calculator \
  aiagent:latest "create a new file called hello.txt with content 'Hello Docker!'"
```

### Verbose mode
```bash
docker run --rm --env-file .env -v $(pwd)/calculator:/app/calculator \
  aiagent:latest "read main.py" --verbose
```

## Interactive Mode

Run the container interactively:
```bash
docker run -it --rm --env-file .env \
  -v $(pwd)/calculator:/app/calculator \
  --entrypoint /bin/bash \
  aiagent:latest
```

Then inside the container:
```bash
uv run main.py "your question here"
```

## Environment Variables

Create a `.env` file with:
```
GEMINI_API_KEY=your_api_key_here
```

## Volume Mounts

The calculator directory is mounted so the agent can:
- Read and analyze code
- Run tests
- Create/modify files
- Execute Python scripts

## Notes

- The container runs as root by default
- Changes to mounted volumes persist on the host
- API rate limits still apply (wait between requests)
- Use `--verbose` flag for detailed output
