import math

class Cylinder(object):

    def __init__(self, height=1, radius=1):
        self.height = height
        self.rad = radius

    def volume(self):
        vol = 0.0
        vol = math.pi * self.rad**2 *self.height

        return vol

    def surface_area(self):
        area = 0.0
        areap1 = (2 * math.pi * self.rad * self.height) * 1.0
        areap2 = (2 * math.pi * self.rad**2) * 1.0
        area = areap1 + areap2
        
        return area
