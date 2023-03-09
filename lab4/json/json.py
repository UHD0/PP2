
import json

with open("data.json", "r") as f:
    a = f.read()
data = json.loads(a)
dn = de = sp = mt = ""
print("""
Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------
""")

for i in range(len(data["imdata"])):
    dn = data["imdata"][i]["l1PhysIf"]["attributes"]["dn"]
    de = data["imdata"][i]["l1PhysIf"]["attributes"]["descr"]
    sp = data["imdata"][i]["l1PhysIf"]["attributes"]["speed"]
    mt = data["imdata"][i]["l1PhysIf"]["attributes"]["mtu"]
    print("{:<49}{:<23}{:<7}  ".format(dn, de, sp), mt)