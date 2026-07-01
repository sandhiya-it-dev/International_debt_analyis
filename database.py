import os
from dotenv import load_dotenv,find_dotenv
from sqlalchemy import create_engine

# Load environment variables
load_dotenv(find_dotenv())

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")


def get_engine():
    connection_string = (
        f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}"
        f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

    engine = create_engine(connection_string)

    return engine


if __name__ == "__main__":
    try:
        engine = get_engine()

        with engine.connect():
            print("✅ Connected to PostgreSQL successfully!")

    except Exception as e:
        print("❌ Connection failed!")
        print(e)