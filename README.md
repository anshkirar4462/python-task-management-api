# Python Task Management REST API

A RESTful API built with Python and FastAPI to manage tasks using CRUD operations, SQLite database storage, API key authentication, request validation, and automated testing.

## 🚀 Features

- **REST API:** Built using FastAPI.
- **CRUD Operations:** Create, read, update, and delete tasks.
- **Database Integration:** SQLite database with SQLAlchemy ORM.
- **API Authentication:** API key authentication using the `X-API-Key` header.
- **Data Validation:** Request validation using Pydantic.
- **Interactive Documentation:** Test endpoints through Swagger UI.
- **Automated Testing:** Test API functionality using Pytest and HTTPX.
- **Error Handling:** Handles invalid requests, missing tasks, and unauthorized access.

## 🛠️ Technologies Used

- Python
- FastAPI
- Uvicorn
- SQLite
- SQLAlchemy
- Pydantic
- Pytest
- HTTPX
- Git and GitHub

## 📁 Project Structure

```text
python-task-management-api/
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
├── tasks.db
└── tests/
    └── test_main.py
```

**Note:** `tasks.db` is generated locally by the application and is excluded from version control. It may not appear in the GitHub repository.

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/python-task-management-api.git
cd python-task-management-api
```

Replace `YOUR-USERNAME` with your GitHub username.

### 2. Install dependencies

Make sure Python is installed. Then run:

```bash
python -m pip install -r requirements.txt
```

If the `python` command is unavailable on Windows, use the full path to your Python executable.

### 3. Start the application

```bash
python -m uvicorn main:app --reload
```

The API will be available at:

- Homepage: http://127.0.0.1:8000
- Health check: http://127.0.0.1:8000/health
- Interactive API documentation: http://127.0.0.1:8000/docs

## 🔐 Authentication

Task endpoints require an API key supplied through the `X-API-Key` header.

For local development, the example key configured in the source code is:

```text
my-secret-key
```

In Swagger UI, click **Authorize**, enter the key, and authorize the requests.

**Security note:** The example API key is intended only for development. Production applications should load secrets from environment variables or a secret manager and avoid committing credentials to GitHub.

## 📡 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | API homepage |
| GET | `/health` | Health check |
| POST | `/tasks` | Create a task |
| GET | `/tasks` | Retrieve all tasks |
| GET | `/tasks/{task_id}` |