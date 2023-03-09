import re
s = "Hel_lo_ World"
p = '^$'
x = re.findall(p, s)
print(x)