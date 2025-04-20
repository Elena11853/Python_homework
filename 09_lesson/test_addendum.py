
from sqlalchemy import create_engine
db_connection_string = "postgresql://postgres:Beklin@localhost:5432/QA"
db = create_engine(db_connection_string)


