import os

path = input()

try:
    os.chdir(path)
    dirs = os.listdir(os.getcwd())
    for i in dirs:
        if os.path.isdir(i):
            print(f'<DIR> {i}')
        elif os.path.isfile(i):
            print(f'<FILE> {i}')
except:
    print('Такой папки не существует!')