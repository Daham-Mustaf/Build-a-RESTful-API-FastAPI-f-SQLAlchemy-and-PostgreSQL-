
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine=create_engine("postgresql://postgres:postgres@localhost/item_db",
    echo=True
)

Base=declarative_base()
SessionLocal=sessionmaker(bind=engine)


# while True:

#     try:
#         conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres',
#                                 password='password123', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connection was succesfull!")
#         break
#     except Exception as error:
#         print("Connecting to database failed")
#         print("Error: ", error)
#         time.sleep(2)