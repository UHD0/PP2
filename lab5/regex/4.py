import re
p = '^a+b*'
string = "acbbbbbbb"
x = re.findall(p, string)
print(x)