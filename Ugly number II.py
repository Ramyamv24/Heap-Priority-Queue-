from heapq import heappush, heappop

class Solution(object):
    def nthUglyNumber(self, n):
        primes = [2, 3, 5]
        uglyHeap = [1]
        visited = set()
        visited.add(1)

        for _ in range(n):
            curr = heappop(uglyHeap)
            for prime in primes:
                new_ugly = curr * prime
                if new_ugly not in visited:
                    heappush(uglyHeap, new_ugly)
                    visited.add(new_ugly)

        return curr


def main():
    n = int(input("Enter n: "))

    obj = Solution()
    result = obj.nthUglyNumber(n)

    print("The", n, "th ugly number is:", result)


if __name__ == "__main__":
    main()