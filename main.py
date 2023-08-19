from fastapi import FastAPI, HTTPException
from typing import List
from pydantic import BaseModel
from datetime import datetime
import databases
import sqlalchemy

DATABASE_URL = "sqlite:///./db.sqlite"

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)

class Transaction(BaseModel):
    user_id: int
    full_name: str
    transaction_date: datetime
    transaction_amount: float
    transaction_type: str

transactions = sqlalchemy.Table(
    "transactions",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, index=True),
    sqlalchemy.Column("user_id", sqlalchemy.Integer),
    sqlalchemy.Column("full_name", sqlalchemy.String),
    sqlalchemy.Column("transaction_date", sqlalchemy.DateTime),
    sqlalchemy.Column("transaction_amount", sqlalchemy.Float),
    sqlalchemy.Column("transaction_type", sqlalchemy.String),
)

app = FastAPI()

# ----------------------------------------------------------- Endpoints
# for testing
@app.get("/hello", status_code=200)
def hello():
    return {"mesage": "Hello world"}

@app.post("/transactions/", response_model=Transaction)
async def create_transaction(transaction: Transaction) -> Transaction:
    """
    Create a new transaction.

    Parameters:
        - transaction: The transaction object containing the details of the transaction.

    Returns:
        - Transaction: The created transaction object with the generated transaction ID.
    """
    query = transactions.insert().values(
        user_id=transaction.user_id,
        full_name=transaction.full_name,
        transaction_date=datetime.now(),
        transaction_amount=transaction.transaction_amount,
        transaction_type=transaction.transaction_type,
    )
    transaction_id = await database.execute(query)
    return {**transaction.dict(), "id": transaction_id}

@app.get("/transactions/{user_id}", response_model=List[Transaction])
async def read_user_transactions(user_id: int) -> List[Transaction]:
    """
    Retrieves a list of transactions for a specific user.

    Args:
        user_id (int): The ID of the user.

    Returns:
        List[Transaction]: A list of Transaction objects representing the user's transactions.
    """
    query = transactions.select().where(transactions.c.user_id == user_id)
    result = await database.fetch_all(query)
    return result

@app.put("/transactions/{transaction_id}", response_model=Transaction)
async def update_transaction(transaction_id: int, updated_transaction: Transaction) -> Transaction:
    """
    Update a transaction in the database.

    Parameters:
        - transaction_id (int): The ID of the transaction to be updated.
        - updated_transaction (Transaction): The updated transaction data.

    Returns:
        - Transaction: The updated transaction object.

    Example Usage:
        transaction_id = 123
        updated_transaction = Transaction(
            user_id=456,
            full_name="John Doe",
            transaction_date=datetime.now(),
            transaction_amount=100.0,
            transaction_type="debit"
        )
        updated_transaction = await update_transaction(transaction_id, updated_transaction)
    """
    query = (
        transactions.update()
        .where(transactions.c.id == transaction_id)
        .values(
            user_id=updated_transaction.user_id,
            full_name=updated_transaction.full_name,
            transaction_date=datetime.now(),
            transaction_amount=updated_transaction.transaction_amount,
            transaction_type=updated_transaction.transaction_type,
        )
    )
    await database.execute(query)
    return {**updated_transaction.dict(), "id": transaction_id}

@app.delete("/transactions/{transaction_id}", response_model=Transaction)
async def delete_transaction(transaction_id: int) -> Transaction:
    """
    Deletes a transaction with the given ID.

    Parameters:
    - transaction_id (int): The ID of the transaction to be deleted.

    Returns:
    - Transaction: The deleted transaction.
    """
    query = transactions.delete().where(transactions.c.id == transaction_id)
    deleted_transaction = await database.execute(query)
    return deleted_transaction

@app.get("/user_stats/{user_id}")
async def get_user_stats(user_id: int) -> dict:
    """
    Retrieves the statistics of a user based on their user ID.

    Args:
        user_id (int): The ID of the user.

    Returns:
        dict: A dictionary containing the user ID, average transaction amount, and the highest transaction day.

    Raises:
        HTTPException: If the user is not found.
    """
    query = transactions.select().where(transactions.c.user_id == user_id)
    user_transactions = await database.fetch_all(query)
    if not user_transactions:
        raise HTTPException(status_code=404, detail="User not found")

    total_amount = sum(t["transaction_amount"] for t in user_transactions)
    average_transaction = total_amount / len(user_transactions)

    transaction_dates = [t["transaction_date"].date() for t in user_transactions]
    highest_transaction_day = max(set(transaction_dates), key=transaction_dates.count)

    return {
        "user_id": user_id,
        "average_transaction": average_transaction,
        "highest_transaction_day": highest_transaction_day
    }

# Run the application
if __name__ == "__main__":
    import uvicorn
    # uvicorn.run(app, host="0.0.0.0", port=8000)
    uvicorn.run(app, host="localhost", port=8001)