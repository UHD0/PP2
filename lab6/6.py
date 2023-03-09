import os

path = input()

try:
    os.chdir(path)
    for i in range(65, 91):
        output = open(chr(i)+'.txt', 'w')
except Exception as e:
    print(e)