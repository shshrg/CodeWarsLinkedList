from preloaded import Node

'''
Node is defined in preloaded like this:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
    
def push(head, data):
    node = Node(data)
    if head:
        node.next = head
    return node

def build_one_two_three():
    # Your code goes here.
    n1 = Node(3)
    n2 = Node(2)
    n2.next = n1
    n3 = Node(1)
    n3.next = n2
    return n3