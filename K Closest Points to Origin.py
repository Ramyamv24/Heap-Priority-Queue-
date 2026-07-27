import heapq
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Max-heap: store (-distance, point), so largest distance is at top
        heap = []
        
        for x, y in points:
            dist = x * x + y * y  # no need for sqrt, relative order is the same
            heapq.heappush(heap, (-dist, x, y))
            if len(heap) > k:
                heapq.heappop(heap)  # remove the farthest point
        
        return [[x, y] for _, x, y in heap]


# Main part
if __name__ == "__main__":
    points = [[1, 3], [-2, 2], [5, 8], [0, 1]]
    k = 2

    solution = Solution()
    result = solution.kClosest(points, k)

    print("The", k, "closest points to the origin are:")
    print(result)