class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Vector:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end