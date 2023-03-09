#Write the definition of a Point class. Objects from this class should have a method show to display the coordinates of the point
import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print("x:", self.x, "y:", self.y)
    def move(self):
        dx = int(input())
        dy = int(input())
        self.x = dx
        self.y = dy
    def dist(self):
        print(math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2)))

x = int(input())
y = int(input())
p = Point(x, y)
p.show()
p.move()
p.show()
p.dist()