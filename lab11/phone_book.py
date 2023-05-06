import psycopg2
from config import data
import csv
import re

conn = psycopg2.connect(**data)
conn.autocommit = True
cursor = conn.cursor()

def check(s): 

    return bool(re.match(r"\b\+?[7,8](\s*\d{3}\s*\d{3}\s*\d{2}\s*\d{2})\b", s)) 

def show_users():
    print('Choose [A]ll or a [F]ew? [G]o Back')
    action = input()
    if action == 'G':
        return
    if action == 'A':
        creating_function = """
        CREATE OR REPLACE FUNCTION select_all_users()
        RETURNS SETOF phone_book
        LANGUAGE plpgsql
        AS $$
        BEGIN
            RETURN QUERY SELECT * FROM phone_book ORDER BY id;
        END;
        $$;
        """

        cursor.execute(creating_function)
        query = 'SELECT * FROM select_all_users()'
        cursor.execute(query)

        for i in cursor.fetchall():
            print(*i, sep='\n')
            print('\n\n')

    if action == 'F':
        print('Insert the name or phone number')
        to_search = input() + '%'
        creating_function = '''
        CREATE OR REPLACE FUNCTION search(name VARCHAR)
            RETURNS TABLE (
                id integer,
                person_name VARCHAR,
                phone_number VARCHAR
            )
        AS $$
        BEGIN
            RETURN QUERY SELECT *
            FROM phone_book AS pb
            WHERE pb.person_name ILIKE name OR pb.phone_number ILIKE name;
        END; $$
        LANGUAGE PLPGSQL;
        
        SELECT * FROM search(%s)'''

        cursor.execute(creating_function, [to_search])
        for i in cursor.fetchall():
            print(*i)

        
def create_user(name, phone_number):
    query = f"""
    CREATE OR REPLACE PROCEDURE insert_data(name varchar, ph_number varchar)
    LANGUAGE plpgsql
    AS $$
    BEGIN
        UPDATE phone_book SET phone_number = ph_number WHERE person_name = name;
        IF NOT FOUND THEN
            INSERT INTO phone_book (person_name, phone_number) VALUES (name, ph_number);
        END IF;
    END;
    $$;
    SELECT * from phone_book
    WHERE person_name = %s
    """

    if not check(phone_number):
        print('Number invalid')
        new_number = input('Insert new valid number: ')
        create_user(name, new_number)
        return

    cursor.execute(query, [name])
    if cursor.fetchone() == None:
        print('User succesfully added\n\n')
    else:
        print('User succesfully updated\n\n')
    query = 'call insert_data(%s, %s)'  
    cursor.execute(query, [name, phone_number])

    


def read_user():
    print('Insert Part of Name or Part of Phone number')
    data = '%' + input() + '%'
    query = '''
    CREATE OR REPLACE FUNCTION search(name VARCHAR)
        RETURNS TABLE (
            id integer,
            person_name VARCHAR,
            phone_number VARCHAR
        )
    AS $$
    BEGIN
        RETURN QUERY SELECT *
        FROM phone_book AS pb
        WHERE pb.person_name ILIKE name OR pb.phone_number ILIKE name;
    END; $$
    LANGUAGE PLPGSQL;
    
    SELECT * FROM search(%s)'''

    cursor.execute(query, [data])
    print(cursor.fetchone())
    return cursor.fetchone()


def update_person():
    print('If the user does not exist, a new user will be created\nName will be "New name parameter"')
    old_name =         input('Enter old name:         ')
    new_name =         input('Enter name:             ')
    new_phone_number = input('Enter new phone number: ')

    if not check(new_phone_number):
        print('\n\nNumber invalid\n\n')
        update_person()
        return

    query = '''
    CREATE OR REPLACE PROCEDURE update_users(old_name varchar,name varchar, ph_number varchar)
    LANGUAGE plpgsql
    AS $$
    BEGIN
        UPDATE phone_book SET phone_number= ph_number, person_name = name
        where person_name = old_name;
        IF NOT FOUND THEN
            insert into phone_book (person_name, phone_number)
            values (old_name, ph_number);
        end if;
    END;
    $$;
    
    call update_users(%s, %s, %s);
    '''
    get_user = '''SELECT * from phone_book
                  where person_name=%s'''
    cursor.execute(get_user, [old_name])
    is_exists = False
    if cursor.fetchone() != None:
        is_exists = True

    cursor.execute(query, [old_name, new_name, new_phone_number])
    if is_exists:
        print('\n\n\nUser updated\n\n\n')
    else:
        print('\n\n\nNew user created\n\n\n')

def delete_user():
    print('Insert the name of user u want to delete:')
    name = input()
    get_user = 'SELECT * from phone_book WHERE person_name=%s'
    cursor.execute(get_user, [name])
    if cursor.fetchone() == None:
        print('\n\nUser not exists\n\n')
        return
    
    query = '''
    CREATE OR REPLACE PROCEDURE delete_user(user_name varchar)
    LANGUAGE plpgsql
    AS
    $$
    BEGIN
        DELETE FROM phone_book WHERE person_name=user_name;
    END;
    $$;
    
    call delete_user(%s);
    '''
    cursor.execute(query, [name])
    print('\n\n\nPerson has been deleted\n\n\n')

def upload_from_csv():
    with open('users.csv', 'r') as read_file:
        file = csv.reader(read_file)
        for i in file:
            name, surname, phone_number = i[0], i[1], i[2]
            create_user(name, phone_number)

def pagination():
    query = """ 
    SELECT * FROM phone_book ORDER BY id LIMIT %s OFFSET %s; 
    """ 
    limit =  input('\n\nInsert the limit of rows: ')
    offset = input('\n\nInsert the number of rows u want to skip: ')

    cursor.execute(query, [limit, offset])
    for i in cursor.fetchall():
        print(*i, sep='\n')
        print('\n\n')



while True:
    print('[C]reate | [R]ead | [L]ist | [U]pdate | [D]elete | [UP]load data from CSV | [P]agination | [E]xit')
    action = input()

    if action == 'C':
        name = input('Insert the name: ')
        phone_number = input('Insert the phone_number: ')
        create_user(name, phone_number)
    elif action == 'R':
        read_user()
    elif action == 'L':
        show_users()
    elif action == 'U':
        update_person()
    elif action == 'D':
        delete_user()
    elif action == 'UP':
        upload_from_csv()
    elif action == 'P':
        pagination()
    elif action == 'E':
        break

cursor.close()
conn.close()