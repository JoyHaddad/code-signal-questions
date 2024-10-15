# Move Until Obstacle Game

## Problem Description

You are given an array of `n` integers, ranging from 1 to 100 inclusive. Each integer represents a player's progress on a linear gameboard, indicating how many steps they can move to the right. However, the course is fraught with challenges; several obstacles are represented by negative integers.

Your task is to return a **transformed array** structuring the gameboard in a new way:
- If an integer can lead the player to an obstacle on its right (within the range of its value), replace the number with the **index of the obstacle**.
- If the number represents an obstacle (a negative integer), replace it with `-1`.
- If none of these conditions are met, retain the **original integer**.

Keep in mind:
- The array will have no more than 500 elements.
- The elements in the array range from -100 to 100, inclusive.

This task is an innovative take on our previous analysis lesson, implementing a "Move Until Obstacle" game. Good luck with your coding journey!

## Example

Given the input array:

```python
[3, 2, -3, 1, 2]
```
The output should be:
```python
[2, 2, -1, 1, 2]
```
