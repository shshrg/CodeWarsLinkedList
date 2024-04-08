class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
def alternating_split(head):
    if not head or not head.next:
        raise ValueError
    head1 = None
    head2 = None
    tail1 = None
    tail2 = None
    x = True

    current = head
    while current:
        if x:
            if not head1:
                head1 = Node(current.data)
                tail1 = head1
            else:
                tail1.next = Node(current.data)
                tail1 = tail1.next
        else:
            if not head2:
                head2 = Node(current.data)
                tail2 = head2
            else:
                tail2.next = Node(current.data)
                tail2 = tail2.next
        current = current.next
        x = not x
    return Context(head1, head2)
