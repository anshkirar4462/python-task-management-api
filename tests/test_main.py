
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "Task Management API is running!"


def test_create_task():
    response = client.post(
        "/tasks",
        headers={"X-API-Key": "my-secret-key"},
        json={
            "title": "Automated test task",
            "description": "Testing task creation",
            "completed": False
        }
    )
    assert response.status_code == 201
    assert response.json()["title"] == "Automated test task"


def test_get_tasks():
    response = client.get(
        "/tasks",
        headers={"X-API-Key": "my-secret-key"}
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_authentication_required():
    response = client.get("/tasks")
    assert response.status_code == 401


def test_invalid_task():
    response = client.post(
        "/tasks",
        headers={"X-API-Key": "my-secret-key"},
        json={
            "title": "",
            "description": "Invalid task",
            "completed": False
        }
    )
    assert response.status_code == 422



def test_update_task():
    create_response = client.post(
        "/tasks",
        headers={"X-API-Key": "my-secret-key"},
        json={
            "title": "Task to update",
            "description": "Testing update",
            "completed": False
        }
    )
    task_id = create_response.json()["id"]

    response = client.put(
        f"/tasks/{task_id}",
        headers={"X-API-Key": "my-secret-key"},
        json={"completed": True}
    )

    assert response.status_code == 200
    assert response.json()["completed"] is True


def test_delete_task():
    create_response = client.post(
        "/tasks",
        headers={"X-API-Key": "my-secret-key"},
        json={
            "title": "Task to delete",
            "description": "Testing deletion",
            "completed": False
        }
    )
    task_id = create_response.json()["id"]

    response = client.delete(
        f"/tasks/{task_id}",
        headers={"X-API-Key": "my-secret-key"}
    )

    assert response.status_code == 200

    get_response = client.get(
        f"/tasks/{task_id}",
        headers={"X-API-Key": "my-secret-key"}
    )
    assert get_response.status_code == 404
