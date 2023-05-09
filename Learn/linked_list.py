class Node:
    def __init__(self, data):
        self.data = data
        self.next_element = None


class LinkedList:
    def __init__(self):
        self.head_node = None

    # Time: O(1)
    def get_head(self):
        return self.head_node

    # Time: O(1)
    def is_empty(self):
        if self.head_node is None:
            return True
        else:
            return False

    def insert_at_head(self, data):
        temp_node = Node(data)
        temp_node.next_element = self.head_node
        self.head_node = temp_node
        return self.head_node


def insert_at_tail(lst, value):
    new_node = Node(value)

    if lst.get_head() is None:
        lst.head_node = new_node
        return

    temp = lst.get_head()

    while temp.next_element:
        temp = temp.next_element

    temp.next_element = new_node
    return


def delete(data):
    pass


def delete_at_head():
    pass


def search(node, value):
    if not node:
        return False

    if node.data is value:
        return True

    return search(node.next_element, value)


def is_empty():
    pass


