import re

text = input()
arr = text.split()

for i in range(len(arr) - 1):
    res1 = re.match('[A-Z]', arr[i])
    res2 = re.match('[A-Z]', arr[i + 1])
    if res1 and res2:
        arr.insert(i + 1, "    ")
s = ' '.join(arr)
print(s)