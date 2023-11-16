import random
import time

# Deterministic QuickSort
def deterministic_partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def deterministic_quicksort(arr, low, high):
    if low < high:
        pi = deterministic_partition(arr, low, high)
        deterministic_quicksort(arr, low, pi - 1)
        deterministic_quicksort(arr, pi + 1, high)

# Randomized QuickSort
def randomized_partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    return deterministic_partition(arr, low, high)

def randomized_quicksort(arr, low, high):
    if low < high:
        pi = randomized_partition(arr, low, high)
        randomized_quicksort(arr, low, pi - 1)
        randomized_quicksort(arr, pi + 1, high)

# Analysis
def analyze_quicksort():
    arr = input("Enter the array elements separated by space: ").split()
    arr = [int(x) for x in arr]

    print(f"Input Array: {arr}")

    arr_deterministic = arr.copy()
    arr_randomized = arr.copy()

    print("Deterministic QuickSort:")
    start_time = time.time()
    deterministic_quicksort(arr_deterministic, 0, len(arr_deterministic) - 1)
    print(f"Sorted array: {arr_deterministic}")
    print(f"Execution time: {time.time() - start_time:.6f} seconds\n")

    print("Randomized QuickSort:")
    start_time = time.time()
    randomized_quicksort(arr_randomized, 0, len(arr_randomized) - 1)
    print(f"Sorted array: {arr_randomized}")
    print(f"Execution time: {time.time() - start_time:.6f} seconds\n")

if __name__ == "__main__":
    analyze_quicksort()
