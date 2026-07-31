from typing import List
import heapq

class Solution:
    def mincostToHireWorkers(
        self, quality: List[int], wage: List[int], k: int
    ) -> float:

        # (wage/quality ratio, quality)
        ratio = sorted([(w / q, q) for w, q in zip(wage, quality)])

        max_heap = []
        quality_sum = 0
        max_ratio = 0.0

        # First k workers
        for i in range(k):
            max_ratio = max(max_ratio, ratio[i][0])
            quality_sum += ratio[i][1]
            heapq.heappush(max_heap, -ratio[i][1])  # Max heap using negative values

        res = max_ratio * quality_sum

        # Process remaining workers
        for i in range(k, len(quality)):
            max_ratio = max(max_ratio, ratio[i][0])

            # Remove largest quality and add current quality
            quality_sum += ratio[i][1] + heapq.heappop(max_heap)

            heapq.heappush(max_heap, -ratio[i][1])

            res = min(res, max_ratio * quality_sum)

        return res


# ---------------- Main ----------------
if __name__ == "__main__":
    n = int(input("Enter number of workers: "))

    quality = list(map(int, input("Enter quality of workers: ").split()))
    wage = list(map(int, input("Enter minimum wage of workers: ").split()))

    k = int(input("Enter value of k: "))

    sol = Solution()
    ans = sol.mincostToHireWorkers(quality, wage, k)

    print("Minimum Cost to Hire Workers:", round(ans, 5))