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
        # Set the shortest distance to infinity, so we will always find a shorter point
        shortest_distance = math.inf
        shortest_pairs = None
        # Find all the unique pairs of points in the list
        pairs = set(list(itertools.combinations(points, 2)))
        # Unpack each tuple from the pairs
        for p1, p2 in pairs:
            # Calculate the distance between each pair using the Pythagorean Theorem
            distance = math.sqrt(((p2.x - p1.x) ** 2) + ((p2.y - p1.y) ** 2))
            # If we find a closer point, grab this one
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
        """
        Returns a list of points representing the smallest convex ployhedron/polygon containing
        all the points. This uses the Gift Wrapping Algorithm.
        """
        # Define a small helper function to find the determinant of three points
        def determinant(p1: Point, p2: Point, p3: Point) -> float:
            """
            We need this function to find the rotation from point to point.

            Return > 0: Counter-clockwise rotation
            Return < 0: Clockwise rotation
            Return = 0: Collinear
            """
            return (p2.x - p1.x) * (p3.y - p1.y) - (p2.y - p1.y) * (p3.x - p1.x)
        # Find the left most point, we'll use this as our starting point
        # This point will always be in the hull, as being leftmost guarantees it
        # to be on the outside
        leftmost_point = Point(math.inf, math.inf)
        for point in points:
            if point.x < leftmost_point.x:
                leftmost_point = point
        # Set the current point to the leftmost point, our starting point
        current_point = leftmost_point
        # Create the hull list, with the first value being the leftmost point
        hull = [leftmost_point]
        # Set the next point value to the second point in the list
        next_point = points[1]
        # Set the current index to the third point, since we already have the second point
        i = 2
        while True:
            # If its a clockwise rotation
            if determinant(current_point, next_point, points[i]) < 0:
                # Set the next point to the current point in the list
                next_point = points[i]
            # Increment the index by one
            i += 1
            # If we are not at the end of the list, skip the rest of the iteration
            if i != len(points):
                continue
            # If the next point equals our initial starting point, end the search
            if next_point == leftmost_point:
                break
            # Reset the index value
            i = 0
            # Add the next point to the hull
            hull.append(next_point)
            # Set the current point to the next point, essentially "incrementing" what point we are at
            current_point = next_point
            # Set the next point to the leftmost point, resetting our value
            next_point = leftmost_point
        # Return the hull points list
        return hull    

    def largest_empty_circle(self, points: list[Point]) -> tuple[Point, float]:
        """
        Given a list of points, finds the largest circle within its center inside of their 
        covex hull and enclosing none of them.

        Returns tuple(Center of circle, diameter)
        """
        convex_hull = self.get_convex_hull(points)