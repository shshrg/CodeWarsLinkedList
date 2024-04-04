""" For your information:
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
"""

def sorted_insert(head, data):
    all_data = []
    while isinstance(head, Node):
        all_data.append(head.data)
        head = head.next
#     all_data.append(head.data)
    all_data.append(data)
    all_data.sort(reverse=True)
    print(all_data)
    result = None
    for i in all_data:
        n1 = Node(i)
        n1.next = result
        result = n1
    return result