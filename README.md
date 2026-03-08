# MSCS532 Assignment 1
## Insertion Sort (Monotonically Decreasing Order)

### Overview
This repository contains a Python implementation of the Insertion Sort algorithm that sorts an array in monotonically decreasing order (largest to smallest).

The algorithm is based on the insertion sort method described in *Introduction to Algorithms (CLRS), Chapter 2*.

Insertion sort works by iteratively taking one element from the input list and inserting it into the correct position in the sorted portion of the list.

---

### Algorithm Description

Insertion Sort builds the final sorted array one element at a time.

Steps:
1. Start with the second element in the list.
2. Compare it with the element before it.
3. Shift elements that are smaller than the current element to the right.
4. Insert the element in its correct position.
5. Repeat until the entire list is sorted.

For this assignment, the comparison is modified so that the list is sorted in **monotonically decreasing order**.

---

### Python Implementation

```python
def insertion_sort_decreasing(arr):

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr
```

---

### Example

Input:

[31, 41, 59, 26, 41, 58]

Output:

[59, 58, 41, 41, 31, 26]

---

### How to Run

1. Clone the repository

```git clone https://github.com/YOUR_USERNAME/MSCS532_Assignment1.git```

2. Navigate to the folder

```cd MSCS532_Assignment1``` 

3. Run the program

```python insertion_sort_decreasing.py```
