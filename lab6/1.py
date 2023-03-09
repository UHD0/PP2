import os

path = input()

os.chdir(path)

dirs = os.listdir(os.getcwd())
for i in dirs:
    if os.path.isdir(i):
        print(f'<DIR> {i}')
    elif os.path.isfile(i):
        print(f'<FILE> {i}')