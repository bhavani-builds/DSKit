# Contributing to DSKit

Thank you for your interest in contributing! 🎉

## Getting Started

1. Fork the repository
2. Clone your fork:
   ```bash
   git clone https://github.com/yourusername/dskit.git
   cd dskit
   ```
3. Create a virtual environment and install in dev mode:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Windows: .venv\Scripts\activate
   pip install -e ".[dev]"
   ```

## Development Workflow

- **Run tests:** `pytest tests/ -v`
- **Format code:** `black dskit/`
- **Lint:** `ruff check dskit/`

## Adding a New Command

1. Add your command function to `dskit/commands.py`
2. Register the subparser in `dskit/cli.py`
3. Add tests in `tests/test_commands.py`
4. Document it in `README.md`

## Pull Request Guidelines

- Keep PRs focused on one feature or fix
- Include tests for new functionality
- Update `README.md` if you add new commands or options
- Run `black` and `ruff` before submitting

## Reporting Issues

Please include:
- Your OS and Python version
- The command you ran
- The full error output
