# Array Rotation for Minimum Manhattan Distance

## Problem Description

Given two arrays, `array1` and `array2`, both of size `n` where `n` ranges from **1 to 500** (inclusive), your task is to find a **rotation of `array1`** that results in the **smallest possible Manhattan distance** to `array2`.

Each integer in `array1` and `array2` is a non-negative integer with a maximum value of **10³**.

### Definitions

1. **Manhattan Distance** between two arrays `a` and `b` of size `n` is given by:
   \[
   D(a, b) = \sum\_{i=1}^n |a_i - b_i|
   \]
   where \(a_i\) and \(b_i\) denote the i-th elements of `a` and `b`, respectively.

2. A **rotation** of an array is an operation where one or more elements from the end of the array are moved to the beginning, while maintaining the order of the moved elements.

3. **Objective**:
   - Find the rotation of `array1` that **minimizes the Manhattan distance** with `array2`.
   - If multiple rotations yield the same minimum distance, return the rotated array which has the smallest value when all elements are concatenated into a single integer.

### Output

The function should return:

- The **rotated array of `array1`** that results in the smallest possible Manhattan distance.
- The **minimum Manhattan distance** value.

### Example

Given:

```python
array1 = [3, 4, 1, 2]
array2 = [1, 2, 3, 4]
```

The possible rotations of `array1` are:

```python
[3, 4, 1, 2]
[4, 1, 2, 3]
[1, 2, 3, 4]
[2, 3, 4, 1]
```

Calculating Manhattan distance for each rotation with `array2`:

```python
For [3, 4, 1, 2], Manhattan distance is 8.
For [4, 1, 2, 3], Manhattan distance is 4.
For [1, 2, 3, 4], Manhattan distance is 0.
For [2, 3, 4, 1], Manhattan distance is 8.
```

The minimum Manhattan distance is `0` for the rotation `[1, 2, 3, 4]`.
