import psycopg2
from config import data

conn = psycopg2.connect(**data)
cursor = conn.cursor()

cursor.close()
conn.close()