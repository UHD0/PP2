import re
p = """
Heeeeeellllooooooo
. - любой символ
^ - начало строки
$ - конец строки
* - любое количество повторений
"""
s = "Heeeeeellllooooooo"
pattern = "H+e+l+o+"
print(re.findall(pattern, s))