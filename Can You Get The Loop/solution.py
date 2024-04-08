def loop_size(node):
    slow = node
    fast = node
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            k = 1
            slow = slow.next
            while slow != fast:
                slow = slow.next
                k += 1
            return k
        