# Swap Linked List Nodes

## Description

This function swaps the nodes of a given singly linked list at two specified indices, `start` and `end` (both 0-based).

- The function should only modify the `next` property of the nodes, not their values.
- It is guaranteed that `start <= end`.

## Function Signature

```python
def swap_linked_list_nodes(head: ListNode, start: int, end: int) -> ListNode:
    """
    Swaps the nodes at the given indices in a singly linked list.
    """

## Example

### Input
- **Linked List:** `1 -> 2 -> 3 -> 4 -> 5`
- **start:** `1`
- **end:** `3`

### Output
- **Linked List:** `1 -> 4 -> 3 -> 2 -> 5`

## Time Complexity
The expected time complexity is **O(n)**, where `n` is the length of the linked list.
```
