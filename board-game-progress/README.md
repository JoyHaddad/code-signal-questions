# Board Game Progress Calculation

## Problem Description

You are the developer of a unique board game and need to quantify player progress, assuming different starting positions.

### Game Setup:

- The game is played on a **linear board** represented by an array of integers, where each integer denotes a **move value** a player can take. The move value signifies how many steps a player can move **rightward**.
- The size of the board (`n`) ranges from **1 to 500**, inclusive.
- The goal is for the player to reach the **end of the board** starting from various positions, but there are **obstacles** on certain positions that players cannot land on.
- An **obstacle** is represented by a specific integer value. If a player encounters an obstacle, they cannot progress further.

### Task:

You are to implement the `solution(numbers, obstacle)` function, which calculates and returns an array `steps`. The array `steps` contains the number of moves required for a player to reach the end of the array from each starting position `i`. If the player cannot reach the end due to an obstacle, the value in `steps[i]` should be `-1`.

### Input:

- `numbers`: An array of integers where each element represents the number of steps a player can move from that position. Each value in `numbers` ranges from **1 to 10**, inclusive.
- `obstacle`: An integer representing the obstacle value. If a player lands on this value, they cannot progress further. The obstacle value ranges from **1 to 10**, inclusive.

### Output:

- Return an array `steps` where each element `steps[i]`:
  - Represents the number of moves required to reach the end of the array starting from position `i`.
  - If the player encounters an obstacle and cannot progress, `steps[i]` should be `-1`.

## Example

Given the input:

```python
numbers = [5, 3, 2, 6, 2, 1, 7]
obstacle = 3
```

The function should return:

```python
[3, -1, 3, 1, 2, 2, 1]
```
