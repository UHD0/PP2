import math
def volume(r):
    return 4/3*3.14*(math.pow(r, 3))

r = float(input())
print(volume(r))