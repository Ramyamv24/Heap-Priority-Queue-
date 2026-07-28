from collections import deque
from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[] for _ in range(n)]

        for u, v, w in flights:
            adj[u].append((v, w))

        dist = [float("inf")] * n
        dist[src] = 0

        queue = deque([(src, 0)])
        stops = 0

        while queue and stops <= k:
            size = len(queue)
            temp_dist = dist[:]

            for _ in range(size):
                city, cost = queue.popleft()

                for next_city, price in adj[city]:
                    if cost + price < temp_dist[next_city]:
                        temp_dist[next_city] = cost + price
                        queue.append((next_city, cost + price))

            dist = temp_dist
            stops += 1

        return -1 if dist[dst] == float("inf") else dist[dst]


def main():
    n = 4
    flights = [
        [0, 1, 100],
        [1, 2, 100],
        [2, 3, 100],
        [0, 2, 500]
    ]
    src = 0
    dst = 3
    k = 1

    sol = Solution()
    result = sol.findCheapestPrice(n, flights, src, dst, k)

    print("Number of cities:", n)
    print("Flights:", flights)
    print("Source:", src)
    print("Destination:", dst)
    print("Maximum stops:", k)
    print("Cheapest Price:", result)


if __name__ == "__main__":
    main()