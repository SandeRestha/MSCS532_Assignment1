"""
MSCS532 - Assignment 1
Insertion Sort Algorithm (Monotonically Decreasing Order)

This program implements the Insertion Sort algorithm
and sorts numbers from largest to smallest.
"""

def insertion_sort_decreasing(arr):
    """
    Sort a list in monotonically decreasing order
    using the insertion sort algorithm.

    Parameters:
    arr (list): list of numbers

    Returns:
    list: sorted list (largest to smallest)
    """

    # Loop through array starting from second element
    for i in range(1, len(arr)):

        # Store the current value to insert
        key = arr[i]

        # Compare with previous elements
        j = i - 1

        # Shift elements smaller than key to the right
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1

        # Insert key into correct position
        arr[j + 1] = key

    return arr


if __name__ == "__main__":

    # Example list of numbers
    numbers = [31, 41, 59, 26, 41, 58]

    print("Original Array:")
    print(numbers)

    # Perform insertion sort
    sorted_numbers = insertion_sort_decreasing(numbers)

    print("\nSorted Array (Monotonically Decreasing):")
    print(sorted_numbers)