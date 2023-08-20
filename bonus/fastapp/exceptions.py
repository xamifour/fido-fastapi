from fastapi import HTTPException

class TransactionNotFoundError(HTTPException):
    def __init__(self):
        super().__init__(status_code=404, detail="Transaction not found")
