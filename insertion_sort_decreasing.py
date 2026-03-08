"""
MSCS532 - Assignment 1
Insertion Sort (Monotonically Decreasing Order)
"""

def insertion_sort_decreasing(arr):
    """
    Sorts an array in monotonically decreasing order
    using the Insertion Sort algorithm.
    """

    # Traverse array starting from the second element
    for i in range(1, len(arr)):

        # Element to be inserted into sorted section
        key = arr[i]

        # Index of the previous element
        j = i - 1

        # Move smaller elements one position to the right
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1

        # Insert key at correct location
        arr[j + 1] = key

    return arr


if __name__ == "__main__":
    numbers = [31, 41, 59, 26, 41, 58]
    print("Original Array:", numbers)