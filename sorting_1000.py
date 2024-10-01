import random
import time

# Import sorting functions from previous file or copy them here
from divide_conquer_sorting import merge_sort, quick_sort
from sortings import insertion_sort, bubble_sort, selection_sort  # Assumes sortings.py is in the same directory

# Function to measure execution time of sorting algorithms
def measure_time(sort_function, arr):
    start_time = time.time()
    sort_function(arr)
    end_time = time.time()
    return end_time - start_time

if __name__ == "__main__":
    # Generate an array of 1000 random integers
    array_size = 1000
    random_array = [random.randint(0, 10000) for _ in range(array_size)]

    # Measure and print time for each sorting algorithm
    algorithms = {
        "Insertion Sort": insertion_sort,
        "Bubble Sort": bubble_sort,
        "Selection Sort": selection_sort,
        "Merge Sort": merge_sort,
        "Quick Sort": quick_sort
    }

    # Record execution time for each algorithm
    execution_times = {}
    for name, sort_function in algorithms.items():
        arr_copy = random_array.copy()  # Copy the array to ensure the same input for each algorithm
        print(f"Testing {name}...")
        exec_time = measure_time(sort_function, arr_copy)
        execution_times[name] = exec_time
        print(f"{name} took {exec_time:.6f} seconds")

    # Display results
    print("\nExecution Time Summary:")
    for name, time_taken in execution_times.items():
        print(f"{name}: {time_taken:.6f} seconds")
