class Point:

    def __init__(self,x,y):
        self.x_cod = x
        self.y_cod = y

    def __str__(self):
        return '<{},{}>'.format(self.x_cod,self.y_cod)

    def distance(self,other):
        return ((other.x_cod - self.x_cod)**2 +(other.y_cod - self.y_cod)**2)**0.5

    def distance_from_origin(self):
        return (self.x_cod**2 + self.y_cod**2)**0.5


class Line:

    def __init__(self,A,B,C):
        self.A = A
        self.B = B
        self.C = C

    def __str__(self):
        return '{}x + {}y + {}'.format(self.A,self.B,self.C)

    def point_on_line(line,point):
        if line.A*point.x_cod + line.B*point.y_cod + line.C ==0:
            return "point lies on the line"
        else:
            return "point does not lies on the line"

    def shortest_distance(line,point):
        return abs(line.A*point.x_cod + line.B*point.y_cod + line.C)/((line.A**2 +line.B**2)**0.5)
        

    

p1 = Point(3,2)
p2 = Point(1,10)
print(p1.distance(p2))
print(p2.distance_from_origin())
l1 = Line(1,1,-2)
print(l1)
print(p2)
print(l1.point_on_line(p2))
print(l1.shortest_distance(p2))
