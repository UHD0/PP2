import math

n = int(input())
l = int(input())

h = l / 2 * math.tan(math.radians(180 / n))

print((h * l * n) / 2)