# This code simply has examples of three basic sorting algorithms
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

# --- Demonstrations ---

print("--- Bubble Sort ---")
unsorted_list_bubble = [64, 34, 25, 12, 22, 11, 90]
print(f"Original list: {unsorted_list_bubble}")
sorted_list_bubble = bubble_sort(list(unsorted_list_bubble)) # Use list() to create a copy
print(f"Sorted list (Bubble Sort): {sorted_list_bubble}")

print("\n--- Quick Sort ---")
unsorted_list_quick = [10, 7, 8, 9, 1, 5]
print(f"Original list: {unsorted_list_quick}")
sorted_list_quick = quick_sort(list(unsorted_list_quick)) # Use list() to create a copy
print(f"Sorted list (Quick Sort): {sorted_list_quick}")

print("\n--- Merge Sort ---")
unsorted_list_merge = [38, 27, 43, 3, 9, 82, 10]
print(f"Original list: {unsorted_list_merge}")
sorted_list_merge = merge_sort(list(unsorted_list_merge)) # Use list() to create a copy
print(f"Sorted list (Merge Sort): {sorted_list_merge}")
