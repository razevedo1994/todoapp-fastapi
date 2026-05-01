# FastAPI TODO App

A RESTful TODO API built with FastAPI and Python 3.12+. This is a learning project focused on exploring FastAPI fundamentals — routing, Pydantic schemas, and testing with pytest.

## Tech Stack

- **[FastAPI](https://fastapi.tiangolo.com/)** — web framework
- **[Pydantic v2](https://docs.pydantic.dev/)** — data validation and serialization
- **[Uvicorn](https://www.uvicorn.org/)** — ASGI server
- **[pytest](https://pytest.org/) + pytest-cov** — testing and coverage
- **[Ruff](https://docs.astral.sh/ruff/)** — linting and formatting
- **[Taskipy](https://github.com/taskipy/taskipy)** — task runner aliases

## Project Structure

```
todoapp-fastapi/
├── app/
│   ├── main.py               # FastAPI app entry point
│   ├── pyproject.toml        # Dependencies, ruff config, task aliases
│   ├── IMPROVEMENTS.md       # Known limitations and next steps
│   ├── api/
│   │   └── v1/
│   │       └── routers/
│   │           ├── tasks.py  # Task CRUD endpoints
│   │           └── users.py  # User CRUD endpoints
│   ├── core/
│   │   └── user_id_validation.py  # Shared get_or_404 helper
│   └── schemas/
│       ├── tasks.py          # Task Pydantic models + Status enum
│       └── user.py           # User Pydantic models
└── tests/
    ├── conftest.py            # Shared pytest fixtures
    ├── test_main.py           # Root endpoint test
    └── api/v1/routers/
        └── test_users.py      # User route tests
```

## Getting Started

**Prerequisites:** Python 3.12+

```bash
# Clone the repository
git clone https://github.com/your-username/todoapp-fastapi.git
cd todoapp-fastapi/app

# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -e ".[dev]"
```

## Running the App

All task commands must be run from inside the `app/` directory.

```bash
cd app
task run
```

The server starts at `http://127.0.0.1:8000` with hot-reload enabled.

Interactive API docs are available at:
- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## Available Commands

| Command | Description |
|---------|-------------|
| `task run` | Start the development server with hot-reload |
| `task test` | Run lint checks then all tests with coverage |
| `task lint` | Check code style with Ruff |
| `task format` | Auto-fix and format app source code |
| `task format_test` | Auto-fix and format test code |

## API Overview

### Users

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/users/` | Create a new user |
| `GET` | `/users/` | List all users |
| `GET` | `/users/{user_id}` | Get a user by ID |
| `PUT` | `/users/{user_id}` | Update a user |
| `DELETE` | `/users/{user_id}` | Delete a user |

### Tasks

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/tasks/?user_id={id}` | Create a task for a user |
| `GET` | `/tasks/{user_id}` | List all tasks for a user |
| `PUT` | `/tasks/{user_id}/{task_id}` | Update a task |

**Task status values:** `pending`, `doing`, `completed`

### Example: Create a User

```bash
curl -X POST "http://127.0.0.1:8000/users/" \
  -H "Content-Type: application/json" \
  -d '{"username": "alice", "email": "alice@example.com", "password": "secret"}'
```

### Example: Create a Task

```bash
curl -X POST "http://127.0.0.1:8000/tasks/?user_id=1" \
  -H "Content-Type: application/json" \
  -d '{"task": "Buy groceries", "priority": "high", "status": "pending"}'
```

## Running Tests

```bash
cd app
task test
```

This runs Ruff lint checks followed by pytest with coverage report for the `app/` directory.

To run tests only (skip lint):

```bash
cd app
pytest ../tests --cov=. -vv
```

## Limitations & Improvements

See [app/IMPROVEMENTS.md](app/IMPROVEMENTS.md) for a list of known limitations and planned next steps.
