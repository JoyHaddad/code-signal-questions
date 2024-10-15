# 1D Game Path Evaluation

## Problem Description

Your task is to design a 1-dimensional game where a player moves along a path determined by an array of integers.

### Path Characteristics:

- The path is an array of integers, where each element ranges from **-100 to 100**, inclusive.
- The size of the array (`n`) ranges from **1 to 500**, inclusive.
- Each integer `a_i` in the array signifies the number of steps the player can move and the initial direction:
  - A **positive integer** allows the player to move that many steps to the **right**.
  - A **negative integer** directs the player to move that many steps to the **left**.
  - **Zero** signifies a blockade that **prevents further movement**.

### Game Rules:

1. The player **starts at the first position** of the array (index 0) and moves according to the value at the current position.
2. If the value in the current position is **zero**, the game ends.
3. If the player's move leads them **outside the array boundaries**, they reverse direction and continue moving. In this reversed state:
   - Positive integers move the player to the **left**.
   - Negative integers move the player to the **right**.
4. The game ends if:
   - The player **encounters a blockade** (a zero).
   - The player **reaches the array boundaries** for the **second time** and can no longer move.
5. It is guaranteed that the game will not lead to an infinite loop.

## Task

You are to implement a function titled `evaluatePath(numbers)`. This function should take an array of integers as input, representing the path and its rules, and return a tuple `(position, moves)` where:

- **position**: The player's final position (0-indexed) when the game ends.
- **moves**: The total number of moves made by the player until the game ends.

## Example

Given the input array:

```python
[3, 4, 1, 1, -3, 1]
```

The function should return:

```python
(4, 5)
```
