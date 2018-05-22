import math

class Line(object):

        def __init__(self, coor1, coor2):
            self.coor1 = coor1
            self.coor2 = coor2
            pass

        def distance(self):
            distance = 0.0
            x = (self.coor2[0] - self.coor1[0]) * 1.0
            y = (self.coor2[1] - self.coor1[1]) * 1.0
            distance = x**2 + y**2
            distance = math.sqrt(distance)

            return distance

        def slope(self):
            slope = 0.0
            dy = (self.coor2[1] - self.coor1[1]) * 1.0
            dx = (self.coor2[0] - self.coor1[0]) * 1.0

            slope = dy/dx

            return slope

