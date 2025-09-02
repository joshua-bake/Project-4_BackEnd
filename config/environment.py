import os

db_URI = os.getenv("DATABASE_URL", None)
SECRET = os.getenv("SECRET", "northstoppaintzebra")

if db_URI.startswith("postgres://"):
    db_URI = db_URI.replace("postgres://", "postgresql://", 1)
