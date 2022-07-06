from objects import Point, Vector
from intersect import intersect
from BST import Node, BST

def any_intersect(segments: list[Vector]):
    points = []
    points_segments = {}

    for segment in segments:
        p1 = segment.start
        p2 = segment.end

        points.append(p1)
        points.append(p2)

        points_segments[p1] = segment
        points_segments[p2] = segment

    points.sort(key=lambda  p: p.x)

    tree = BST()

    for point in points:
        segment = points_segments[point]
        if point is segment.start:
            node = Node(point.y, segment)
            tree.insert(node)

            if tree.successor(point.y) is not None and intersect(tree.successor(point.y)):
                pass
