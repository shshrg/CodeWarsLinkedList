from preloaded import Node

def swap_pairs(head):
    if not head or not head.next:
        return head
    current = head
    new = current.next
    while True:
        a = current.next
        b = a.next
        a.next = current
        if not b or not b.next:
            current.next = b
            break
        current.next = b.next
        current = b
    return new