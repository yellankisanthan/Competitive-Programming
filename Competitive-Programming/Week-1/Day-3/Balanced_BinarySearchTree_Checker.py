import unittest

def is_BST(root,min=-10000000,max=10000000):
    if root is None:
        return True
    if not min<root.value<max:
        return False
    return is_BST(root.left,min,root.value) and is_BST(root.right,root.value,max)
    
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
result = is_BST(tree1)
expected = True
print("test_valid_full_tree: "+str(result==expected))

tree2 = BinaryTreeNode(50)
left = tree2.insert_left(30)
right = tree2.insert_right(80)
left.insert_left(20)
left.insert_right(60)
right.insert_left(70)
right.insert_right(90)
result = is_BST(tree2)
expected = False
print("test_valid_full_tree: "+str(result==expected))

tree3 = BinaryTreeNode(50)
left = tree3.insert_left(40)
left_left = left.insert_left(30)
left_left_left = left_left.insert_left(20)
left_left_left.insert_left(10)
result = is_BST(tree3)
expected = True
print("test_descending_linked_list: "+str(result==expected))

tree4 = BinaryTreeNode(50)
right = tree4.insert_right(70)
right_right = right.insert_right(60)
right_right.insert_right(80)
result = is_BST(tree4)
expected = False
print("test_out_of_order_linked_list: "+str(result==expected))

tree5 = BinaryTreeNode(50)
result = is_BST(tree5)
expected = True
print("test_one_node_tree: "+str(result==expected))