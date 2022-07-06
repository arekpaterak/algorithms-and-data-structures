from objects import Point, Vector
import numpy as np

def position(vector: Vector, point: Point):
    matrix = np.array([[vector.start.x, vector.start.y, 1], [vector.end.x,vector.end.y, 1], [point.x, point.y, 1]])
    determinant = np.linalg.det(matrix)

    return determinant