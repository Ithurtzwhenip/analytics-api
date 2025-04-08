from decouple import config as decouple_config

DATABASE_URL = decouple_config("DATABASE_URL", default="")

# Fix scheme if needed
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql+psycopg://", 1)

DB_TIMEZONE = decouple_config("DB_TIMEZONE", default="UTC")
