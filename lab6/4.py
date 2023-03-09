import os

path = input('Введите путь до папки в которой находится файл -> ')

try:
    os.chdir(path)
    txt = input('Введите название файла с его расширением -> ')
    output = open(txt, 'r')
    output = output.read().split('\n')

    print(f'Количество строк: {len(output)}')
except Exception as e:
    print(e)