from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
import os
from dotenv import load_dotenv
load_dotenv()

# Load environment variables 
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
name = os.getenv("DB_NAME")

# Creates new database connection
engine = create_engine(f"postgresql://{user}:{password}@{host}/{name}")

# Creates base class for all ORM models
Base = declarative_base()

# Creates session factory
Session = sessionmaker()