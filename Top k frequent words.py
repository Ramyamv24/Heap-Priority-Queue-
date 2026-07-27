import heapq
from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)

        # Negate frequency so the min-heap behaves like a max-heap
        heap = [(-freq, word) for word, freq in count.items()]
        heapq.heapify(heap)

        return [heapq.heappop(heap)[1] for _ in range(k)]


# Main part
if __name__ == "__main__":
    words = ["i", "love", "leetcode", "i", "love", "coding"]
    k = 2

    solution = Solution()
    result = solution.topKFrequent(words, k)

    print("Top", k, "frequent words:", result)