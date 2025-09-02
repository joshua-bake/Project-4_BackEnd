import os

db_URI = os.getenv("DATABASE_URL", "postgres://ufpgthp67r151s:p65ce261a3bc3ce8ce6d3aba3d89afebde0eb6c8bc7cabab73d236e563e527436@c9pbiquf6p6pfn.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/d4h8ch80qpevdp")
SECRET = os.getenv("SECRET", "northstoppaintzebra")

if db_URI.startswith("postgres://"):
    db_URI = db_URI.replace("postgres://", "postgresql://", 1)
