import psycopg2
from config import data

conn = psycopg2.connect(**data)
conn.autocommit = True
cursor = conn.cursor()



def create_table():
    query = """
        CREATE TABLE IF NOT EXISTS phone_book (
            id serial primary key,
            person_name varchar(255),
            phone_number varchar(255)
        );
    """
    cursor.execute(query)

create_table()

cursor.close()
conn.close()