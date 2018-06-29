def inorder(lst,node):
    if node==None: 
        return None

    inorder(lst,node.right)

    lst.append(node.value)
    if len(lst) >= 2: 
        return None

    inorder(lst,node.left)

def find_second_largest(root):
    if root == None: raise ValueError()
    lst = []
    inorder(lst,root)
    return lst[1]

# Tests

class BinaryTreeNode(object):

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

tree1 = BinaryTreeNode(50)
left = tree1.insert_left(30)
right = tree1.insert_right(70)
left.insert_left(10)
left.insert_right(40)
right.insert_left(60)
right.insert_right(80)
actual = find_second_largest(tree1)
expected = 70
print(actual == expected)

tree2 = BinaryTreeNode(50)
left = tree2.insert_left(30)
right = tree2.insert_right(70)
left.insert_left(10)
left.insert_right(40)
right.insert_left(60)
actual = find_second_largest(tree2)
expected = 60
print(actual == expected)

tree3 = BinaryTreeNode(50)
left = tree3.insert_left(30)
right = tree3.insert_right(70)
left.insert_left(10)
left.insert_right(40)
right_left = right.insert_left(60)
right_left_left = right_left.insert_left(55)
right_left.insert_right(65)
right_left_left.insert_right(58)
actual = find_second_largest(tree3)
expected = 65
print(actual == expected)

tree4 = BinaryTreeNode(50)
left = tree4.insert_left(30)
tree4.insert_right(70)
left.insert_left(10)
left.insert_right(40)
actual = find_second_largest(tree4)
expected = 50
print(actual == expected)

tree5 = BinaryTreeNode(50)
left = tree5.insert_left(40)
left_left = left.insert_left(30)
left_left_left = left_left.insert_left(20)
left_left_left.insert_left(10)
actual = find_second_largest(tree5)
expected = 40
print(actual == expected)

tree6 = BinaryTreeNode(50)
right = tree6.insert_right(60)
right_right = right.insert_right(70)
right_right.insert_right(80)
actual = find_second_largest(tree6)
expected = 70
print(actual == expected)