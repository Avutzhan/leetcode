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


def insert_at_tail(data):
    pass


def delete(data):
    pass


def delete_at_head():
    pass


def search(data):
    pass


def is_empty():
    pass


