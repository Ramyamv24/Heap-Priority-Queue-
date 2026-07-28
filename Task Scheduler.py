import heapq
from collections import Counter, deque
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        
        # Max-heap of remaining counts (negated for max-heap behavior)
        heap = [-c for c in count.values()]
        heapq.heapify(heap)
        
        time = 0
        cooldown = deque()  # stores (available_time, -remaining_count)
        
        while heap or cooldown:
            time += 1
            
            if heap:
                cnt = heapq.heappop(heap) + 1  # process one instance
                if cnt < 0:
                    # Still has remaining instances; put it in cooldown
                    cooldown.append((time + n, cnt))
            
            # If a task has finished cooling down, push it back to the heap
            if cooldown and cooldown[0][0] == time:
                heapq.heappush(heap, cooldown.popleft()[1])
        
        return time


def main():
    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 2

    sol = Solution()
    result = sol.leastInterval(tasks, n)

    print("Tasks:", tasks)
    print("Cooldown:", n)
    print("Minimum intervals required:", result)


if __name__ == "__main__":
    main()