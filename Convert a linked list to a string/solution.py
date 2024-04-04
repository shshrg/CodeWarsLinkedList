def stringify(node):
    current_node = node
    result = ''
    while current_node:
        result += str(current_node.data)
        current_node = current_node.next
        result += ' -> '
    result += 'None'
    return result