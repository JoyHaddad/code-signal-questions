class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val     # Holds the value or data of the node
        self.next = next  # Points to the next node in the linked list; default is None

def swap_linked_list_nodes(head, start, end):
    #make dummy node for edge cases
    dummy_node = ListNode(0)
    dummy_node.next = head
    prev = dummy_node
    current = head
    count = 0
    
    #find nodes at current and previous index placement
    while current:
        if count == start:
            start_node = current
            prev_start = prev
        if count == end:
            end_node = current
            prev_end = prev
        prev = current
        current = current.next
        count += 1
        
    #swap nodes
    prev_start.next = end_node
    prev_end.next = start_node
    temp_start_node = start_node.next
    start_node.next = end_node.next
    end_node.next = temp_start_node
    
    return dummy_node.next