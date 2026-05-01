# Improvements & Known Limitations

This document tracks known limitations in the current implementation and concrete next steps for each.

---

## 1. In-Memory Storage

**Issue:** Data is stored in plain Python lists and dicts (`user_database = []`, `tasks_database = defaultdict(list)`). All data is lost on every server restart.

**Next step:** Introduce a real database. A lightweight option for a learning project is SQLite via SQLAlchemy (sync) or SQLAlchemy async + `aiosqlite`. For production, swap the connection URL for PostgreSQL.

```
pip install sqlalchemy alembic
```

---

## 2. Plaintext Passwords

**Issue:** The `password` field is stored as a plain string with no hashing.

**Next step:** Hash passwords before storing using `passlib` with `bcrypt`:

```python
from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"])
hashed = pwd_context.hash(plain_password)
```

---

## 3. No Authentication

**Issue:** All endpoints are publicly accessible. There is no login flow, no token validation, and no way to associate a request with a specific user.

**Next step:** Implement OAuth2 with JWT tokens using `python-jose` and FastAPI's `OAuth2PasswordBearer`. FastAPI's own docs have a full walkthrough: https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/

---

## 4. Fragile ID Management

**Issue:** User IDs are generated as `len(user_database) + 1`. Deleting a user shifts the expected IDs, breaking lookups for all subsequent users.

**Next step:** Let the database handle ID generation via auto-increment primary keys. This is a natural consequence of fixing item 1.

---

## 5. No Task Delete Endpoint

**Issue:** There is a `DELETE /users/{user_id}` endpoint but no equivalent for tasks. Once created, a task cannot be removed.

**Next step:** Add `DELETE /tasks/{user_id}/{task_id}` to `app/api/v1/routers/tasks.py` and a corresponding test in `tests/api/v1/routers/`.

---

## 6. Unhandled IndexError on Task Update

**Issue:** `PUT /tasks/{user_id}/{task_id}` does `tasks_database[user_id][task_id - 1] = ...` without validating that `task_id` is within range. An out-of-range `task_id` raises an unhandled `IndexError`, returning a 500.

**Next step:** Add a bounds check before the assignment and raise `HTTPException(status_code=404, detail="Task not found")` if the index is invalid. This mirrors the existing `get_or_404` pattern used for users.

---

## 7. Unvalidated Task Priority

**Issue:** The `priority` field on `TaskSchema` is a free-form `str`. Any value is accepted, making it impossible to filter or sort tasks by priority reliably.

**Next step:** Replace `str` with a `Priority` enum, similar to the existing `Status` enum:

```python
class Priority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
```

---

## 8. Shared Test State

**Issue:** `user_database` is a module-level list. The `client` fixture in `conftest.py` does not reset it between tests, so tests in `test_users.py` are order-dependent (test 2 relies on the user created in test 1).

**Next step:** Add teardown logic to the `client` fixture to clear all in-memory stores after each test:

```python
@pytest.fixture
def client():
    from app.api.v1.routers import users, tasks
    users.user_database.clear()
    tasks.tasks_database.clear()
    with TestClient(app) as c:
        yield c
```

---

## 9. Missing Test Coverage

**Issue:** There are no tests for any task endpoint or for `DELETE /users/{user_id}`.

**Next step:** Add `tests/api/v1/routers/test_tasks.py` covering:
- `POST /tasks/` — happy path, invalid user
- `GET /tasks/{user_id}` — returns task list, invalid user
- `PUT /tasks/{user_id}/{task_id}` — update, invalid user, invalid task
- `DELETE /tasks/{user_id}/{task_id}` (once implemented)

And add a test for `DELETE /users/{user_id}` in the existing `test_users.py`.
