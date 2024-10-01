import random
import time

def merge_sort(arr):
    """
    Merge Sort function that sorts an array.
    Time Complexity: O(n log n)
    Space Complexity: O(n) – Uses additional space for merging.
    """
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursively sort both halves
        merge_sort(left_half)
        merge_sort(right_half)

        # Merging the sorted halves
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Check if any element was left
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr

def partition(arr, low, high):
    """
    Partition function used in Quick Sort.
    """
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low=0, high=None):
    """
    Quick Sort function that sorts an array.
    Time Complexity: O(n log n) on average.
    Space Complexity: O(log n) due to recursion stack space.
    """
    if high is None:
        high = len(arr) - 1

    if low < high:
        pi = partition(arr, low, high)

        # Recursively sort elements before and after partition
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
    
    return arr

if __name__ == "__main__":
    # Array for testing merge and quick sort
    test_array = [38, 27, 43, 3, 9, 82, 10]

    print("Original array:", test_array)

    # Merge Sort
    print("\nMerge Sort Steps:")
    sorted_merge = merge_sort(test_array.copy())
    print("Sorted array using Merge Sort:", sorted_merge)

    # Quick Sort
    print("\nQuick Sort Steps:")
    sorted_quick = quick_sort(test_array.copy())
    print("Sorted array using Quick Sort:", sorted_quick)
