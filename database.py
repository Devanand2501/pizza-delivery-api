from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
import os
from urllib.parse import quote_plus
from dotenv import load_dotenv
load_dotenv()

# Load environment variables 
user = os.getenv("DB_USER")
password = quote_plus(os.getenv("DB_PASSWORD"))
host = os.getenv("DB_HOST")
name = os.getenv("DB_NAME")

# Creates new database connection
engine = create_engine(f"postgresql://{user}:{password}@{host}/{name}",echo=True)

'''try:
    engine = create_engine(f"postgresql://{user}:{password}@{host}/{name}")
    connection = engine.connect()
    print("Connection successful")
    connection.close()
except Exception as e:
    print(f"Connection failed: {e}")'''

# Creates base class for all ORM models
Base = declarative_base()

# Creates session factory
Session = sessionmaker(bind=engine)