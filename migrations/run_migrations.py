import os
import sqlalchemy
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData

DATABASE_URL = os.getenv("DATABASE_URL", "mysql+pymysql://testuser:testpass@db:3306/testdb")

engine = create_engine(DATABASE_URL)
metadata = MetaData()

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(50), nullable=False),
    Column("email", String(100), nullable=False),
)

def run_migration():
    metadata.create_all(engine)

    with engine.connect() as conn:
        # check if data already exists
        result = conn.execute(users.select()).fetchall()
        if not result:
            conn.execute(users.insert(), [
                {"name": "Alice", "email": "alice@example.com"},
                {"name": "Bob", "email": "bob@example.com"},
                {"name": "Charlie", "email": "charlie@example.com"},
            ])
            conn.commit()
    print("✅ Migration finished successfully!")

if __name__ == "__main__":
    run_migration()
