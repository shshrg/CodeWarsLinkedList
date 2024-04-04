from preloaded import Node

# class Node(object):
#     """Node class for reference"""
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next
    
def get_nth(node, index):
    if not isinstance(node, Node):
        raise ValueError
    current_index = 0
    while current_index != index:
        if not node.next:
            raise IndexError
        node = node.next
        current_index += 1
    return node
    # Your code goes here.
  