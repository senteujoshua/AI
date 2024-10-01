def insertion_sort(arr):
    """
    Function to perform Insertion Sort on the given array.
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def bubble_sort(arr):
    """
    Function to perform Bubble Sort on the given array.
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def selection_sort(arr):
    """
    Function to perform Selection Sort on the given array.
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


if __name__ == "__main__":
    # Initial array
    arr = [64, 34, 25, 12, 22, 11, 90]

    # Insertion Sort
    print("Insertion Sort:")
    arr_copy = arr.copy()
    print(f"Original array: {arr_copy}")
    print(f"Sorted array: {insertion_sort(arr_copy)}")

    # Bubble Sort
    print("\nBubble Sort:")
    arr_copy = arr.copy()
    print(f"Original array: {arr_copy}")
    print(f"Sorted array: {bubble_sort(arr_copy)}")

    # Selection Sort
    print("\nSelection Sort:")
    arr_copy = arr.copy()
    print(f"Original array: {arr_copy}")
    print(f"Sorted array: {selection_sort(arr_copy)}")
