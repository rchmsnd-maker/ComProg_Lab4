# DATA AND OBSERVATION CODE SNIPPETS

numbers = [3, 7, 2, 9, 5]
target = 9
for i in range(len(numbers)):
    if numbers[i] == target:
        print("Found at index", i)


numbers = [3, 7, 2, 9, 5]
numbers.sort()
target = 7
low = 0
high = len(numbers) - 1

while low <= high:
    mid = (low + high) // 2
    if numbers[mid] == target:
        print("Found at index", mid)
        break
    elif numbers[mid] < target:
        low = mid + 1
    else:
        high = mid - 1


arr = [5, 3, 8, 4, 2]

for i in range(len(arr)):
    for j in range(0, len(arr) - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print(arr)


arr = [5, 3, 8, 4, 2]

for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1

    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = key

print(arr)


arr = [64, 25, 12, 22, 11]

for i in range(len(arr)):
    min_index = i

    for j in range(i + 1, len(arr)):
        if arr[j] < arr[min_index]:
            min_index = j

    arr[i], arr[min_index] = arr[min_index], arr[i]

print(arr)


import time

numbers = list(range(1000000))
target = 999999

start = time.time()

for i in numbers:
    if i == target:
        break

end = time.time()

print("Execution time:", end - start)


numbers = list(range(1000000))
target = 999999

start = time.time()

low, high = 0, len(numbers) - 1

while low <= high:
    mid = (low + high) // 2

    if numbers[mid] == target:
        break

    elif numbers[mid] < target:
        low = mid + 1

    else:
        high = mid - 1

end = time.time()

print("Execution time:", end - start)


student_id = 4754  # replace with your student ID
target = int(str(student_id)[-2:])
print("Target value:", target)


arr = [1, 2, 3, 2, 4]
found = False

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] == arr[j]:
            found = True
            print("Duplicate found:", arr[i])

print("Result:", found)


def fib_iter(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

print(fib_iter(10))


def fib_rec(n):
    if n <= 1:
        return n
    return fib_rec(n - 1) + fib_rec(n - 2)

print(fib_rec(10))


n = 20

start = time.time()
print(fib_iter(n))
end = time.time()

print("Execution time:", end - start)


import random

arr = random.sample(range(1000), 20)
print("Unsorted:", arr)


def bubble_sort(arr):
    n = len(arr)
    comparisons, swaps = 0, 0

    for i in range(n):
        for j in range(0, n - i - 1):

            comparisons += 1

            if arr[j] > arr[j + 1]:
                swaps += 1
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr, comparisons, swaps


print(bubble_sort([5, 3, 8, 4, 2]))


def selection_sort(arr):
    comparisons, swaps = 0, 0

    for i in range(len(arr)):
        min_idx = i

        for j in range(i + 1, len(arr)):
            comparisons += 1

            if arr[j] < arr[min_idx]:
                min_idx = j

        swaps += 1
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr, comparisons, swaps


print(selection_sort([5, 3, 8, 4, 2]))


def insertion_sort(arr):
    comparisons, swaps = 0, 0

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            comparisons += 1
            arr[j + 1] = arr[j]
            swaps += 1
            j -= 1

        arr[j + 1] = key

    return arr, comparisons, swaps


print(insertion_sort([5, 3, 8, 4, 2]))


arr = random.sample(range(1000), 100)

start = time.time()
bubble_sort(arr[:])
end = time.time()

print("Bubble sort time:", end - start)


arr = random.sample(range(1000), 100)

start = time.time()
selection_sort(arr[:])
end = time.time()

print("Selection sort time:", end - start)


arr = random.sample(range(1000), 100)

start = time.time()
insertion_sort(arr[:])
end = time.time()

print("Insertion sort time:", end - start)


print("{:<15} {:<15} {:<15}".format("Algorithm", "Comparisons", "Swaps"))
print("{:<15} {:<15} {:<15}".format("Bubble", 10, 5))
print("{:<15} {:<15} {:<15}".format("Selection", 10, 4))
print("{:<15} {:<15} {:<15}".format("Insertion", 8, 3))