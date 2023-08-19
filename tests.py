import pytest
from datetime import datetime
from fastapi.testclient import TestClient
from main import app, database, transactions


# to simulate requests to FastAPI application.
client = TestClient(app)

# Test data for transactions
test_transaction = {
    "user_id": 1,
    "full_name": "John Doe",
    "transaction_date": datetime.now(),
    "transaction_amount": 100.0,
    "transaction_type": "credit",
}

# Test the hello endpoint
def test_hello():
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello world"}

# Test creating a transaction
def test_create_transaction():
    response = client.post("/transactions/", json=test_transaction)
    assert response.status_code == 200
    assert response.json()["user_id"] == test_transaction["user_id"]
    assert "id" in response.json()

# Test fetching user transactions
def test_read_user_transactions():
    response = client.get("/transactions/1")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# Test updating a transaction
def test_update_transaction():
    updated_transaction = {
        **test_transaction,
        "transaction_amount": 150.0,
        "transaction_type": "debit",
    }
    response = client.put("/transactions/1", json=updated_transaction)
    assert response.status_code == 200
    assert response.json()["transaction_amount"] == updated_transaction["transaction_amount"]
    assert response.json()["transaction_type"] == updated_transaction["transaction_type"]

# Test deleting a transaction
def test_delete_transaction():
    response = client.delete("/transactions/1")
    assert response.status_code == 200
    assert response.json()["user_id"] == test_transaction["user_id"]
    assert "id" in response.json()

# Test fetching user statistics
def test_get_user_stats():
    response = client.get("/user_stats/1")
    assert response.status_code == 200
    assert "user_id" in response.json()
    assert "average_transaction" in response.json()
    assert "highest_transaction_day" in response.json()

# Cleanup after tests
@pytest.fixture(autouse=True)
def cleanup():
    yield
    database.execute(transactions.delete())

