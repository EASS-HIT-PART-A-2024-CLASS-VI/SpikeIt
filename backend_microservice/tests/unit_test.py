import pytest
from unittest.mock import patch
from fastapi.testclient import TestClient
import sys
import os

# Append the app directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from main import app  # Import the FastAPI app

client = TestClient(app)

@pytest.fixture
def mock_httpx_get(mocker):
    """Mock httpx AsyncClient GET requests"""
    return mocker.patch("httpx.AsyncClient.get", new_callable=AsyncMock)

@pytest.fixture
def mock_httpx_post(mocker):
    """Mock httpx AsyncClient POST requests"""
    return mocker.patch("httpx.AsyncClient.post", new_callable=AsyncMock)

def test_root():
    """Test the root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to SpikeIt!"}

def test_create_workout(mock_httpx_post):
    """Test creating a new workout with a mocked API call"""
    mock_httpx_post.return_value.status_code = 200  # Simulate success response
    mock_httpx_post.return_value.json.return_value = {"message": "Workout created successfully"}

    payload = {
        "workout_id": 1,
        "drills": [
            {
                "name": "Spike Drill",
                "duration": 20,
                "equipment": "Ball, Net",
                "type": "Attack",
                "explanation": "Practice spiking over the net"
            }
        ]
    }
    response = client.post("/new_workout/", json=payload)

    assert response.status_code == 200
    assert response.json() == {"message": "Workout created successfully"}
    mock_httpx_post.assert_called_once()

def test_search_drills(mock_httpx_get):
    """Test searching for drills with a mocked API call"""
    mock_httpx_get.return_value.status_code = 200
    mock_httpx_get.return_value.json.return_value = [
        {
            "name": "Spike Drill",
            "duration": 20,
            "equipment": "Ball, Net",
            "type": "Attack",
            "explanation": "Practice spiking over the net"
        }
    ]

    response = client.get("/search_drills/Attack")

    assert response.status_code == 200
    assert len(response.json()) > 0
    mock_httpx_get.assert_called_once()

def test_show_workout(mock_httpx_get):
    """Test retrieving a specific workout with a mocked API call"""
    mock_httpx_get.return_value.status_code = 200
    mock_httpx_get.return_value.json.return_value = [
        {
            "name": "Spike Drill",
            "duration": 20,
            "equipment": "Ball, Net",
            "type": "Attack",
            "explanation": "Practice spiking over the net"
        }
    ]

    response = client.get("/show_workout/1")

    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert response.json()[0]["name"] == "Spike Drill"
    mock_httpx_get.assert_called_once()

def test_show_all_workouts(mock_httpx_get):
    """Test retrieving all workouts with a mocked API call"""
    mock_httpx_get.return_value.status_code = 200
    mock_httpx_get.return_value.json.return_value = [
        {
            "workout_id": 1,
            "drills": [
                {
                    "name": "Spike Drill",
                    "duration": 20,
                    "equipment": "Ball, Net",
                    "type": "Attack",
                    "explanation": "Practice spiking over the net"
                }
            ]
        }
    ]

    response = client.get("/show_all_workouts/")

    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert response.json()[0]["workout_id"] == 1
    mock_httpx_get.assert_called_once()
