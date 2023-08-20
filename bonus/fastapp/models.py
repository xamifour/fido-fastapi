from sqlalchemy import Table, Column, Integer, String, Float, DateTime

import database

# model to create transactions table
transactions = Table(
    "transactions",
    database.metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("user_id", Integer),
    Column("full_name", String),
    Column("transaction_date", DateTime),
    Column("transaction_amount", Float),
    Column("transaction_type", String),
)