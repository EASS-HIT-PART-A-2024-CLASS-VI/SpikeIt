import pytest
import requests
from unittest.mock import patch
import streamlit as st
import frontend_microservice.main  # Ensure correct import path

@pytest.fixture
def mock_requests_get(mocker):
    """Mock requests.get for API calls"""
    return mocker.patch("requests.get")

@pytest.fixture
def mock_requests_post(mocker):
    """Mock requests.post for API calls"""
    return mocker.patch("requests.post")

def test_search_drills(mock_requests_get):
    """Test searching drills by type"""
    mock_requests_get.return_value.status_code = 200
    mock_requests_get.return_value.json.return_value = [
        {
            "name": "Spike Drill",
            "duration": 20,
            "equipment": "Ball, Net",
            "type": "Attack",
            "explanation": "Practice spiking over the net"
        }
    ]
    
    response = requests.get("http://backend_microservice:8000/search_drills/Attack")
    
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert response.json()[0]["name"] == "Spike Drill"
    mock_requests_get.assert_called_once()

def test_add_workout(mock_requests_post):
    """Test adding a new workout"""
    mock_requests_post.return_value.status_code = 200
    mock_requests_post.return_value.json.return_value = {"message": "Workout created successfully"}
    
    workout_data = {
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
    
    response = requests.post("http://backend_microservice:8000/new_workout/", json=workout_data)
    
    assert response.status_code == 200
    assert response.json()["message"] == "Workout created successfully"
    mock_requests_post.assert_called_once()

def test_view_workouts(mock_requests_get):
    """Test retrieving all workouts"""
    mock_requests_get.return_value.status_code = 200
    mock_requests_get.return_value.json.return_value = [
        {
            "workout_id": 1,
            "drills": [
                {
                    "name": "Block Drill",
                    "duration": 15,
                    "equipment": "None",
                    "type": "Defence",
                    "explanation": "Practice blocking"
                }
            ]
        }
    ]
    
    response = requests.get("http://backend_microservice:8000/show_all_workouts/")
    
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert response.json()[0]["workout_id"] == 1
    mock_requests_get.assert_called_once()

