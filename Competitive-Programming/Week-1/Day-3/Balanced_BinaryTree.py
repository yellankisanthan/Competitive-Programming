def is_balanced(node, diff=None, leafDepth=0):
    
    if diff is None:
        diff = []
    
    leafDepth = leafDepth + 1
    
    if node.left is None and node.right is None:
        if leafDepth not in diff:
            diff.append(leafDepth)
        if max(diff)-min(diff)>1:
            return False
        return True
    
    if node.left:
        check = is_balanced(node.left, diff, leafDepth)
        if not check:
            return False
    
    if node.right:
        check = is_balanced(node.right, diff, leafDepth)
        if not check:
            return False
    
    return True

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

tree1 = BinaryTreeNode(5)
left = tree1.insert_left(8)
right = tree1.insert_right(6)
left.insert_left(1)
left.insert_right(2)
right.insert_left(3)
right.insert_right(4)
result = is_balanced(tree1)
print("test_full_tree: "+str(True==result))

tree2 = BinaryTreeNode(3)
left = tree2.insert_left(4)
right = tree2.insert_right(2)
left.insert_left(1)
right.insert_right(9)
result = is_balanced(tree2)
print("test_both_leaves_at_the_same_depth: "+str(True==result))

tree3 = BinaryTreeNode(6)
left = tree3.insert_left(1)
right = tree3.insert_right(0)
right.insert_right(7)
result = is_balanced(tree3)
print("test_both_leaves_at_the_same_depth: "+str(True==result))

tree4 = BinaryTreeNode(6)
left = tree4.insert_left(1)
right = tree4.insert_right(0)
right_right = right.insert_right(7)
right_right.insert_right(8)
result = is_balanced(tree4)
print("test_leaf_heights_differ_by_two: "+str(False==result))

tree5 = BinaryTreeNode(1)
left = tree5.insert_left(5)
right = tree5.insert_right(9)
right.insert_left(8)
right.insert_right(5)
result = is_balanced(tree5)
print("test_three_leaves_total: "+str(True==result))

tree6 = BinaryTreeNode(1)
left = tree6.insert_left(5)
right = tree6.insert_right(9)
right_left = right.insert_left(8)
right.insert_right(5)
right_left.insert_left(7)
result = is_balanced(tree6)
print("test_both_subtrees_superbalanced: "+str(False==result))

tree7 = BinaryTreeNode(1)
result = is_balanced(tree7)
print("test_only_one_node: "+str(True==result))

tree8 = BinaryTreeNode(1)
right = tree8.insert_left(2)
right_right = right.insert_right(3)
right_right.insert_right(4)
result = is_balanced(tree8)
print("test_linked_list_tree: "+str(True==result))