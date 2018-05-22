class Circle:

    def __init__(self, radius, pi):
        self.radius = radius
        self.pi = pi
        print 'Circle created'

    def getArea(self):
        return (self.radius*self.radius*self.pi)
    
    def setRadius(self, radius):
        self.radius = radius
        return 0

    def getRadius(self):
        return self.radius

    def __str__(self):
        return str(self.radius)

c = Circle(1, 3.14)
c.setRadius(2)
print 'Radius is ', c.getRadius()
print 'Area is ', c.getArea()

print c
