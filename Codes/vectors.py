class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Coordinate({0.x:d}, {0.y:d})'.format(self)



coord = Coordinate(121,1)

print(coord.x)