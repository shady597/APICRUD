# test_connection.py
from sqlalchemy import create_engine, text
import os
import db
engine = create_engine(db.DATABASE_URL)

with engine.connect() as conn:
    result = conn.execute(text("SELECT version()"))
    print(result.fetchone())  # Should print PostgreSQL version