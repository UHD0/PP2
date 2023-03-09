import re

text = input()
arr = re.findall('[A-Z]', text)
arr2 = ['_' + i.lower() for i in arr]
cnt = 0

for i in arr:
    r = re.search('[A-Z]+', text)
    if r:
        n = text.find(i)
        text = text[:n] + arr2[cnt] + text[n + 1:]
    cnt += 1
print(text)