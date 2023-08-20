from pydantic import BaseModel
from datetime import datetime

# class TransactionBase(BaseModel):
#     user_id: int
#     full_name: str
#     transaction_date: str
#     transaction_amount: float
#     transaction_type: str

# class TransactionCreate(TransactionBase):
#     pass

# class TransactionUpdate(TransactionBase):
#     pass

# class Transaction(TransactionBase):
#     id: int

class Transaction(BaseModel):
    user_id: int
    full_name: str
    transaction_date: datetime
    transaction_amount: float
    transaction_type: str