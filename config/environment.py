import os

db_URI = os.getenv("DATABASE_URL", "postgresql://localhost:5432/flashcard_db")
SECRET = os.getenv("SECRET", "northstoppaintzebra")

if db_URI.startswith("postgres://"):
    db_URI = db_URI.replace("postgres://", "postgresql://", 1)
