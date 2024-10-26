# Character Numerical Representation Dictionary

## Problem Description

You are given a string of lowercase English alphabets, where the length `n` of the string ranges from **1 to 500**, inclusive.

### Task:

Create a function that returns a dictionary where each key-value pair represents:

- **Key**: An alphabet character `k` present in the string.
- **Value**: The computed numerical representation `v` for each character `k`.

### Computation Rules for Numerical Representation:

1. For each character `k` in the string:
   - Replace `k` with the character that comes **three characters before it** in the alphabetical order (wrapping around to 'z' when this goes below 'a').
   - Multiply the **ASCII value** of this new character by the **frequency of `k`** in the provided string.
2. Store the result as the value associated with `k` in the dictionary.

### Output:

The returned dictionary should:

- Contain only the **alphabetical characters** present in the input string.
- Be **sorted in ascending order by the characters**.

### Constraints

- **1 ≤ n ≤ 500**

### Example

Given the string:

```python
"abc"
```

The output should be:

```python
{'a': 120, 'b': 121, 'c': 122}
```
