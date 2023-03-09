import re
pattern = r"[a-z]"
h = r"\b \ \ \ \ \n"
print(h)
string = "Hello world World1 world2"
print(re.findall(pattern, string))