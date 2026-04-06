# 1. Using defaultdict for Automatic Initialization
# Reduces time complexity when building maps or grouping data
# by avoiding conditional checks.

from collections import defaultdict
graph = defaultdict(list)
graph["A"].append("B")
graph["A"].append("C")
print("Graph:", dict(graph))


# 2. Memoization to Optimize Recursive Functions
# Improves time complexity by caching previous results.
from functools import lru_cache
@lru_cache(maxsize=None)
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
print("Factorial of 5:", factorial(5))


# 3. Two Pointers Technique for O(n) Solutions
# Used for problems involving pairs in sorted arrays.

def has_pair_sum(nums, target):
    nums.sort()
    left, right = 0, len(nums) - 1

    while left < right:
        s = nums[left] + nums[right]
        if s == target:
            return True
        elif s < target:
            left += 1
        else:
            right -= 1
    return False
nums = [2, 7, 11, 15]
target = 9
print("Pair with target sum exists:", has_pair_sum(nums, target))


# 4. Sliding Window Technique
# Reduces nested loops into a single pass.
def max_subarray_sum(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)
    return max_sum
arr = [2, 1, 5, 1, 3, 2]
k = 3
print("Maximum subarray sum:", max_subarray_sum(arr, k))


# 5. Min-Heap with heapq for Efficient Sorting
import heapq
nums = [7, 2, 5, 3, 1]
heapq.heapify(nums)
smallest = heapq.heappop(nums)
print("Smallest element:", smallest)
print("Remaining heap:", nums)