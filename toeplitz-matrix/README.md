# Toeplitz Matrix Checker

## Problem Description

You are given a square matrix of size \( n \times n \), where \( n \) ranges from **1 to 500** (inclusive). A **Toeplitz matrix** is a matrix in which each descending diagonal from left to right contains the same value. Your task is to determine whether the given matrix is a Toeplitz matrix.

### Definition

A matrix is Toeplitz if:

- For all \( i, j \) in the matrix:
  \[
  \text{matrix}[i][j] = \text{matrix}[i+1][j+1]
  \]
  for all valid indices \( i+1 \) and \( j+1 \).

### Output

The function should return:

- `True` if the matrix is a Toeplitz matrix.
- `False` otherwise.

### Example

#### Input

Matrix:

```python
6 7 8
4 6 7
1 4 6
```

#### Output

```python
True
```

The descending diagonals are:

```python
[6], [7, 7], [8]
[4, 4]
[1]
```

Each diagonal contains the same value, so the matrix is a Toeplitz matrix
