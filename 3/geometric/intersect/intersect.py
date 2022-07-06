from objects import Point, Vector
from position_of_point import position

def intersect(segment1: Vector, segment2: Vector) -> bool:
    p1 = segment1.start
    p2 = segment1.end
    p3 = segment2.start
    p4 = segment2.end

    d1 = position(segment2, p1)
    d2 = position(segment2, p2)
    d3 = position(segment1, p3)
    d4 = position(segment1, p4)

    if d1 * d2 < 0 and d3 * d4 < 0:
        return True
    elif d1 == 0 and on_segment(segment2, p1):
        return True
    elif d2 == 0 and on_segment(segment2, p2):
        return True
    elif d3 == 0 and on_segment(segment1, p3):
        return True
    elif d4 == 0 and on_segment(segment1, p4):
        return True
    else:
        return False

def on_segment(segment: Vector, point: Point):
    if (min(segment.start.x, segment.end.x) <= point.x <= max(segment.start.x, segment.end.x)) and (min(segment.start.y, segment.end.y) <= point.y <= max(segment.start.y, segment.end.y)):
        return True
    else:
        return False
