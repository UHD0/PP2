import os

path = input()

try:
    os.chdir(path)
    print(os.access(path, os.W_OK))
except Exception as e:
    print(e)