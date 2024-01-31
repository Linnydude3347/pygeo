"""
A Euclidean 2D dimensional space representation.

Sources/Links:
Gift Wrapping Algorithm Pseudocode: https://en.wikipedia.org/wiki/Gift_wrapping_algorithm
"""

from segment import LineSegment, Point
import math
import itertools

class Plane:

    def closest_pair_points(self, points: list[Point]) -> tuple[Point, Point]:
        """
        Find a pair of points that have the shortest distance between them.
        Returns a tuple containing those two points.
        """
        shortest_distance = math.inf
        shortest_pairs = None
        # Find all the unique pairs of points in the list
        pairs = set(list(itertools.combinations(points, 2)))
        for p1, p2 in pairs:
            # Calculate the distance between each pair
            distance = math.sqrt(((p2.x - p1.x) ** 2) + ((p2.y - p1.y) ** 2))
            if distance < shortest_distance:
                shortest_pairs = (p1, p2)
                shortest_distance = distance
        return shortest_pairs
    
    def get_intersection_points(self, segments: list[LineSegment]) -> list[float]:
        """
        Returns a list of points representing every occurance of line segment intersections.
        """
        # Quick check if there is less than two segments in the list
        if len(segments) < 2:
            return None
        intersection_points = []
        # Find all the unique pairs of segments in the list.
        pairs = set(list(itertools.combinations(segments, 2)))
        # Check for intersections
        for s1, s2 in pairs:
            if s1.intersects_with(s2):
                int_point = s1.get_intersection_point_with(s2)
                intersection_points.append(int_point)
        return intersection_points
    
    def get_convex_hull(self, points: list[Point]) -> list[Point]:
        pass
