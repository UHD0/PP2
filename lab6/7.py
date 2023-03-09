import os

path = input()

try:
    os.chdir(path)
    txt1 = input()
    path2 = input()
    txt2 = input()
    with open(txt1,'r') as input, open(path2 + '/' + txt2, 'a') as output:
        for line in input:
            output.write(line)
except Exception as e:
    print(e)