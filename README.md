# AI Agent

An AI-powered coding agent that can read, write, execute, and analyze Python code using Google's Gemini API.

## Features

- 📁 List and explore directory structures
- 📖 Read file contents
- ✍️ Write and modify files
- 🐍 Execute Python files with arguments
- 🔄 Multi-iteration problem solving
- 🐳 Docker support

## Quick Start

### Prerequisites

- Python 3.13+
- uv (Python package installer)
- Google Gemini API key ([Get one here](https://aistudio.google.com/app/apikey))

### Setup

1. Clone the repository:
```bash
git clone <your-repo-url>
cd AIAgent
```

2. Copy `.env.example` to `.env` and add your API key:
```bash
cp .env.example .env
# Edit .env and add your GEMINI_API_KEY
```

3. Install dependencies:
```bash
uv pip install -r requirements.txt
```

4. Run the agent:
```bash
uv run main.py "what files are in the calculator directory?"
```

## Usage

### Basic Commands

```bash
# List files
uv run main.py "what files are in the root?"

# Read code
uv run main.py "show me the contents of main.py"

# Run tests
uv run main.py "run the tests"

# Create files
uv run main.py "create a README.md file"

# Verbose mode
uv run main.py "your question" --verbose
```

## Docker

### Build and Run

```bash
# Build image
docker build -t aiagent:latest .

# Run container
docker run --rm --env-file .env \
  -v $(pwd)/calculator:/app/calculator \
  aiagent:latest "your question here"

# Docker Compose
docker-compose up
```

See [README_DOCKER.md](README_DOCKER.md) for more Docker options.

## Configuration

Edit `call_function.py` to change the working directory:
```python
args["working_directory"] = "./your-project-path"
```

## Project Structure

```
AIAgent/
├── main.py              # Entry point
├── call_function.py     # Function orchestration
├── prompt.py            # System prompt
├── config.py            # Configuration
├── functions/           # Available functions
│   ├── get_files_info.py
│   ├── get_file_content.py
│   ├── write_file.py
│   └── run_python_file.py
├── calculator/          # Example project
└── tests/              # Test files
```

## Security

- Working directory is restricted to prevent access outside allowed paths
- All file operations are validated
- Environment variables for sensitive data

## License

MIT

## Contributing

Pull requests welcome!
