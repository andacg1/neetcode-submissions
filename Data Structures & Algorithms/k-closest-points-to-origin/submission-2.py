from heapq import *
from math import *
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(point: List[int]) -> int:
            return sqrt((point[0]**2) + (point[1]**2))
        # points = list(map(lambda point: (dist(point), point)))
        point_heap = []
        for point in points:
            heappush_max(point_heap, (dist(point), point))
            while len(point_heap) > k:
                heappop_max(point_heap)
        return list(map(lambda point_tuple: point_tuple[1], point_heap))