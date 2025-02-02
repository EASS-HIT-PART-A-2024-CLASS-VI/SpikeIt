import pytest
from unittest.mock import patch, MagicMock
from fastapi.testclient import TestClient
from db_microservice.main import app
import db_microservice.db_operations as db_ops

client = TestClient(app)

@pytest.fixture
def mock_db(mocker):
    """Mock the SQLite database connection"""
    return mocker.patch("sqlite3.connect", new_callable=MagicMock)

def test_create_db(mock_db):
    """Test database creation"""
    mock_cursor = mock_db.return_value.cursor.return_value
    mock_cursor.execute.return_value = None  # Simulate SQL execution
    db_ops.create_db()
    mock_cursor.execute.assert_called()  # Ensure table creation SQL is executed

def test_add_workout(mock_db):
    """Test adding a workout with mocked DB"""
    mock_cursor = mock_db.return_value.cursor.return_value
    mock_cursor.lastrowid = 1  # Simulate workout_id assignment
    db_ops.add_workout([
        {"name": "Block Drill", "duration": 15, "equipment": "None", "type": "Defence", "explanation": "Practice blocking"}
    ])
    assert mock_cursor.execute.call_count > 1  # Ensure at least one insert occurred

def test_get_workout(mock_db):
    """Test retrieving a specific workout"""
    mock_cursor = mock_db.return_value.cursor.return_value
    mock_cursor.fetchall.return_value = [
        (1, "Block Drill", 15, "None", "Defence", "Practice blocking", 1)
    ]
    mock_cursor.description = [("id",), ("name",), ("duration",), ("equipment",), ("type",), ("explanation",), ("workout_id",)]
    
    result = db_ops.get_workout(1)
    assert isinstance(result, list)
    assert result[0]["name"] == "Block Drill"

def test_get_all_workouts(mock_db):
    """Test retrieving all workouts"""
    mock_cursor = mock_db.return_value.cursor.return_value
    mock_cursor.fetchall.side_effect = [
        [(1,), (2,)],  # Simulate two workout IDs
        [(1, "Block Drill", 15, "None", "Defence", "Practice blocking", 1)],
        [(2, "Spike Drill", 20, "Ball", "Attack", "Jump and spike", 2)]
    ]
    mock_cursor.description = [("id",), ("name",), ("duration",), ("equipment",), ("type",), ("explanation",), ("workout_id",)]
    
    result = db_ops.get_all_workouts()
    assert isinstance(result, list)
    assert len(result) == 2

def test_get_drills_by_type(mock_db):
    """Test retrieving drills by type"""
    mock_cursor = mock_db.return_value.cursor.return_value
    mock_cursor.fetchall.return_value = [
        (1, "Block Drill", 15, "None", "Defence", "Practice blocking", 1)
    ]
    mock_cursor.description = [("id",), ("name",), ("duration",), ("equipment",), ("type",), ("explanation",), ("workout_id",)]
    
    result = db_ops.get_drills_by_type("Defence")
    assert isinstance(result, list)
    assert result[0]["type"] == "Defence"
