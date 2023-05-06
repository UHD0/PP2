import psycopg2
from config import data

connect = psycopg2.connect(**data)
cursor = connect.cursor()

name = input('Введите имя пользователя: ')
query = f'''
select * from snake
where name=\'{name}\'
'''

cursor.execute(query)
is_user = cursor.fetchall()
if(len(is_user) == 0):
    print(r'Такого пользователя нет, желаете создать нового? (y\n)')
    answer = input()
    if answer == 'y':
        new_query = f'''
        insert into snake (name, score)
        values (\'{name}\', 0);
        '''

        cursor.execute(new_query)
        connect.commit()
    else:
        print('Тогда я вам не дам поиграть')
        exit()

cursor.close()
connect.close()
