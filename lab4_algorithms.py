# Step 1: Define an algorithm in pseudocode as comments
# Algorithm to find the largest number in a list
# 1. Assume the first number is the largest
# 2. Compare each number with the current largest
# 3. If a number is larger, update the largest
# 4. Return the largest number

# Step 2: Implement it in Python
numbers = [10, 5, 20, 8, 15]
largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest number:", largest)

# Try It:
# Write pseudocode for finding the smallest number in a list, then implement it in Python.

# Try It Solution
numbers = [10, 5, 20, 8, 15]
smallest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num

print("Smallest number:", smallest)


# 2. Analyze Time Complexity Using Big O
# Step 1: Define a simple linear loop
def print_items(items):
    for item in items:
        print(item)

# Step 2: Observe the number of operations relative to input size
sample = list(range(10))
print_items(sample)  # O(n)

# Try It:
# Create two functions — one that prints pairs (nested loop, O(n²))
# and one that prints just the first item (O(1)).

# Try It Solution

# O(n^2)
def print_pairs(items):
    for i in items:
        for j in items:
            print(i, j)

# O(1)
def print_first(items):
    if len(items) > 0:
        print(items[0])

print_pairs([1,2,3])
print_first([1,2,3])


# 3. Linear Search
# Step 1: Implement linear search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Step 2: Test the function
data = [3, 5, 2, 4, 9]
index = linear_search(data, 4)
print("Found at index:", index)

# Try It:
# Modify the linear search to count the number of comparisons made before finding the target.

# Try It Solution
def linear_search_with_count(arr, target):
    comparisons = 0
    for i in range(len(arr)):
        comparisons += 1
        if arr[i] == target:
            return i, comparisons
    return -1, comparisons

index, comps = linear_search_with_count(data, 4)
print("Found at index:", index)
print("Comparisons made:", comps)


# 4. Binary Search
# Step 1: Implement binary search
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    comparisons = 0

    while low <= high:
        mid = (low + high) // 2
        comparisons += 1

        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1, comparisons

# Step 2: Test with a sorted list
sorted_data = [1, 3, 5, 7, 9, 11]
result, comps = binary_search(sorted_data, 7)
print("Found at index:", result)
print("Binary search comparisons:", comps)


# 5. Bubble Sort (Intro to Sorting)

# Step 1: Implement bubble sort
def bubble_sort(arr):
    n = len(arr)
    swaps = 0

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                swaps += 1
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return swaps

# Step 2: Test sorting
to_sort = [64, 34, 25, 12, 22, 11, 90]
swap_count = bubble_sort(to_sort)

print("Sorted list:", to_sort)
print("Number of swaps:", swap_count)

# Try It:
# Count the number of swaps that occur during the bubble sort of a list.


# 6. Selection Sort

# Step 1: Implement selection sort
def selection_sort(arr):
    comparisons = 0
    swaps = 0

    for i in range(len(arr)):
        min_idx = i

        for j in range(i+1, len(arr)):
            comparisons += 1

            if arr[j] < arr[min_idx]:
                min_idx = j

        swaps += 1
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return comparisons, swaps

# Step 2: Test and observe performance
sample_data = [29, 10, 14, 37, 13]

comparisons, swaps = selection_sort(sample_data)

print("Sorted list:", sample_data)
print("Comparisons:", comparisons)
print("Swaps:", swaps)

# Try It:
# Compare the number of comparisons and swaps in selection sort vs bubble sort.


# 7. Insertion Sort
# Step 1: Implement insertion sort
def insertion_sort(arr):
    comparisons = 0
    swaps = 0

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            comparisons += 1
            arr[j + 1] = arr[j]
            swaps += 1
            j -= 1

        arr[j + 1] = key

    return comparisons, swaps

# Step 2: Test and measure performance
arr = [12, 11, 13, 5, 6]

comparisons, swaps = insertion_sort(arr)

print("Sorted array:", arr)
print("Comparisons:", comparisons)
print("Swaps:", swaps)

# Try It:
# Analyze insertion sort’s performance when the list is already sorted.

sorted_test = [1,2,3,4,5]
comparisons, swaps = insertion_sort(sorted_test)
print("Already sorted list result:", sorted_test)
print("Comparisons:", comparisons, "Swaps:", swaps)


# 8. Comparing Algorithm Efficiency
import time
import random

# Step 1: Generate sample data
data = random.sample(range(10000), 1000)

# Step 2: Compare performance of Python's built-in sort vs bubble sort
start = time.time()
sorted_data = sorted(data)  # Timsort, O(n log n)
print("Built-in sort time:", time.time() - start)

# Step 3: Bubble sort (intentionally slow for demonstration)
def bubble_sort_full(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

# Try It:
# Experiment with different input sizes and compare the runtime of algorithms using the time module.

start = time.time()
bubble_sort_full(data.copy())
print("Bubble sort time:", time.time() - start)