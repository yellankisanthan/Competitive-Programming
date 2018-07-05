def reverse(head):
    next_Node = None
    prev_Node = None
    while head:
        next_Node = head.next
        head.next = prev_Node
        prev_Node = head
        head = next_Node
    return prev_Node
# Tests

class LinkedListNode(object):

    def __init__(self, value, next=None):
        self.value = value
        self.next  = next

    def get_values(self):
        node = self
        values = []
        while node is not None:
            values.append(node.value)
            node = node.next
        return values

def test_short_linked_list():
    second = LinkedListNode(2)
    first = LinkedListNode(1, second)

    result = reverse(first)
    print(result is not None)

    actual = result.get_values()
    expected = [2, 1]
    print(actual == expected)

def test_long_linked_list():
    sixth = LinkedListNode(6)
    fifth = LinkedListNode(5, sixth)
    fourth = LinkedListNode(4, fifth)
    third = LinkedListNode(3, fourth)
    second = LinkedListNode(2, third)
    first = LinkedListNode(1, second)

    result = reverse(first)
    print(result is not None)

    actual = result.get_values()
    expected = [6, 5, 4, 3, 2, 1]
    print(actual == expected)

def test_one_element_linked_list():
    first = LinkedListNode(1)

    result = reverse(first)
    print(result is not None)

    actual = result.get_values()
    expected = [1]
    print(actual == expected)

def test_empty_linked_list():
    result = reverse(None)
    print(result is None)

test_short_linked_list()
test_long_linked_list()
test_one_element_linked_list()
test_empty_linked_list()