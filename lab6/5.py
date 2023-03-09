import os

path = input('Введите путь до папки в которой находится файл -> ')

try:
    os.chdir(path)
    txt = input('Введите название файла с его расширением -> ')
    output = open(txt, 'w')
    output.write(str(list(map(int, input().split()))))
    output.close()
except Exception as e:
    print(e)