from sqlalchemy import create_engine
import os

URL = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('db_port')}/{os.getenv('DB_NAME')}"
engine = create_engine(URL, echo=True)