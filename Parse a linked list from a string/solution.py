def linked_list_from_string(s):
    s = s.split(" -> ")[:-1]
    node = None
    for i, x in enumerate(s[::-1]):
        node = Node(int(x), node)
    return node