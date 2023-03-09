import os

print('Укажите путь: ')
path = input()

try:
    os.chdir(path)
    dirs = os.listdir(os.getcwd())
    print('Выберите папку или файл для удаления: ')
    for i in dirs:
        if os.path.isdir(i):
            print(f'<DIR> {i}')
        elif os.path.isfile(i):
            print(f'<FILE> {i}')
    print('Введите имя файла:')
    name = input()
    if os.access(f'./{name}', os.W_OK):
        os.remove(name)
    else:
        print('Нет доступа к этому файлу')
    
except Exception as e:
    print(e)