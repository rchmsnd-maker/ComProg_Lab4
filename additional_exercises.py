import time

# --- Input Section ---
student_id = "2023-12345" # Use your actual TUP student ID
main_list = list(range(1, 10001)) 
duplicate_list = [14, 25, 67, 89, 32, 45, 67, 10, 99]

# --- Calculations Section ---
target_value = int(student_id[-2:])

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target: return i
    return -1

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target: return mid
        elif arr[mid] < target: low = mid + 1
        else: high = mid - 1
    return -1

def find_duplicate_quadratic(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]: return arr[i]
    return None

# Timing
results = []
for name, func, data, target in [
    ("Linear Search", linear_search, main_list, target_value),
    ("Binary Search", binary_search, main_list, target_value),
    ("Quadratic Search", find_duplicate_quadratic, duplicate_list, None)
]:
    start = time.perf_counter()
    if target is not None: func(data, target)
    else: func(data)
    results.append((name, time.perf_counter() - start))

# --- Output Section ---
print(f"{'Algorithm':<20} | {'Time Taken (s)':<15}")
print("-" * 40)
for name, t in results:
    print(f"{name:<20} | {t:.10f}")