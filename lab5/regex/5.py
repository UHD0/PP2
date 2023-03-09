import re
pattern = "b?"
string = "abbbbbbc acs bca"
print(re.findall(pattern, string))