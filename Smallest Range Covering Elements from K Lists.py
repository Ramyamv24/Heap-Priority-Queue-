from typing import List
import heapq

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap = []
        cur_max = float('-inf')

        # Put the first element of each list into the min-heap
        for i in range(len(nums)):
            heapq.heappush(heap, (nums[i][0], i, 0))
            cur_max = max(cur_max, nums[i][0])

        small = [float('-inf'), float('inf')]

        while heap:
            cur_min, list_idx, idx = heapq.heappop(heap)

            # Update smallest range
            if cur_max - cur_min < small[1] - small[0]:
                small = [cur_min, cur_max]

            # Push next element from the same list
            if idx + 1 < len(nums[list_idx]):
                nxt = nums[list_idx][idx + 1]
                heapq.heappush(heap, (nxt, list_idx, idx + 1))
                cur_max = max(cur_max, nxt)
            else:
                # One list is exhausted
                break

        return small


# ---------------- Main ----------------
if __name__ == "__main__":
    n = int(input("Enter number of lists: "))

    nums = []
    for i in range(n):
        arr = list(map(int, input(f"Enter sorted elements of list {i + 1}: ").split()))
        nums.append(arr)

    sol = Solution()
    ans = sol.smallestRange(nums)

    print("Smallest Range:", ans)