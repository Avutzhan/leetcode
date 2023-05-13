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


def delete(lst, value):
    deleted = False
    if lst.is_empty():
        print("List is Empty")
        return deleted
    current_node = lst.get_head()
    previous_node = None
    if current_node.data == value:
        lst.delete_at_head()
        deleted = True
        return deleted

    while current_node is not None:
        if value == current_node.data:
            previous_node.next_element = current_node.next_element
            current_node.next_element = None
            deleted = True
            break
        previous_node = current_node
        current_node = current_node.next_element

    if deleted == False:
        print(str(value) + " is not in list!")
    else:
        print(str(value) + " deleted!")

    return deleted


def delete_at_head(lst):
    first_element = lst.get_head()

    if first_element is not None:
        lst.head_node = first_element.next_element
        first_element.next_element = None
    return


def search(node, value):
    if not node:
        return False

    if node.data is value:
        return True

    return search(node.next_element, value)


def length(lst):
    # start from the first element
    curr = lst.get_head()
    length = 0

    # Traverse the list and count the number of nodes
    while curr:
        length += 1
        curr = curr.next_element
    return length


def reverse(lst):
    previous = None
    current = lst.get_head()
    nextNode = None

    while current:
        nextNode = current.next_element
        current.next_element = previous
        previous = current
        current = nextNode

        lst.head_node = previous
    return lst


# Floyd's Cycle Finding Algorithm
def detect_loop(lst):
    # Keep two iterators
    onestep = lst.get_head()
    twostep = lst.get_head()
    while onestep and twostep and twostep.next_element:
        onestep = onestep.next_element  # Moves one node at a time
        twostep = twostep.next_element.next_element  # Skips a node
        if onestep == twostep:  # Loop exists
            return True
    return False


def find_mid(lst):
    if lst.is_empty():
        return None

    node = lst.get_head()
    mid = 0
    if lst.length() % 2 == 0:
        mid = lst.length()//2
    else:
        mid = lst.length()//2 + 1

    for i in range(mid - 1):
        node = node.next_element

    return node.data


def remove_duplicates(lst):
    if lst.is_empty():
        return None

    # If list only has one node, leave it unchanged
    if lst.get_head().next_element is None:
        return lst

    outer_node = lst.get_head()
    while outer_node:
        inner_node = outer_node  # Iterator for the inner loop
        while inner_node:
            if inner_node.next_element:
                if outer_node.data == inner_node.next_element.data:
                    # Duplicate found, so now removing it
                    new_next_element = inner_node.next_element.next_element
                    inner_node.next_element = new_next_element
                else:
                    # Otherwise simply iterate ahead
                    inner_node = inner_node.next_element
            else:
                # Otherwise simply iterate ahead
                inner_node = inner_node.next_element
        outer_node = outer_node.next_element

    return lst


def union(list1, list2):
    if list1.is_empty():
        return list2
    elif list2.is_empty():
        return list1

    start = list1.get_head()

    while start.next_element:
        start = start.next_element

    start.next_element = list2.get_head()
    list1.remove_duplicates()
    return list1


def find_nth(lst, n):
    if lst.is_empty():
        return -1

    length = lst.length() - 1

    current_node = lst.get_head()

    position = length - n + 1

    if position < 0 or position > length:
        return -1

    count = 0

    while count is not position:
        current_node = current_node.next_element
        count += 1

    if current_node:
        return current_node.data
    return -1
