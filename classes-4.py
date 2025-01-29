import math
class Point:
    def __init__(self, x,y):
        self.x=x
        self.y=y
    def show(self):
        print(self.x, self.y)
    def move(self,plusx,plusy):
        self.x+=plusx
        self.y+=plusy
    def dist(self, other_point):
        return math.sqrt((self.x-other_point.x)**2+(self.y-other_point.y)**2)
    
point1=Point(1,1)
point2=Point(3,3)

point1.show()
point2.show()

point1.move(5,5)
point1.show()

print("dist:", f"{point2.dist(point1):.2f}")
