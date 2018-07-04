def delete_node(node):

    # Delete the input node from the linked list
    node.value = node.next.value
    node.next = node.next.next

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

fourth = LinkedListNode(4)
third = LinkedListNode(3, fourth)
second = LinkedListNode(2, third)
first = LinkedListNode(1, second)

def evaluate(l1,l2):
    if len(l1)!=len(l2):
        return False
    for i in range(len(l1)):
        if l1[i]!=l2[i]:
            return False
    return True


delete_node(first)
actual = first.get_values()
expected = [2, 3, 4]
print(evaluate(actual,expected))

delete_node(third)
actual = first.get_values()
expected = [2, 4]
print(evaluate(actual,expected))