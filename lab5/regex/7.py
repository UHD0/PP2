import re
pattern = r'\b.+'
string = '123H__el4$3534lo W13225orld'
print(re.findall(pattern, string))