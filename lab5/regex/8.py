import re

text = input()
arr = re.split('[A-Z][a-z]', text)
print(arr)
