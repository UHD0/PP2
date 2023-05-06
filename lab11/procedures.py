import psycopg2
from config import data

conn = psycopg2.connect(**data)
conn.autocommit = True
cursor = conn.cursor()

insert_data = '''
CREATE OR REPLACE PROCEDURE insert_data(name varchar(255), surname varchar(255), phone_number varchar(255))
LANGUAGE plpgsql
AS $$
BEGIN
    -- Try to update an existing user by name
    UPDATE users SET phone = p_phone WHERE name = p_name;
    
    -- If no rows were updated, insert a new user
    IF NOT FOUND THEN
        INSERT INTO users (name, phone) VALUES (p_name, p_phone);
    END IF;
END;
$$;
'''

cursor.execute(insert_data)