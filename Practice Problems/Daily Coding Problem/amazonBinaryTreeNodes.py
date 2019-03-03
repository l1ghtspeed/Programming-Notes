'''
Problem Description:

This problem was asked by Amazon.

Given a complete binary tree, count the number of nodes in faster than O(n) time. Recall that a complete binary tree has every level filled except the last, and the nodes in the last level are filled starting from the left.


'''

def find_left_height(root):
    height = 0
    while root.left:
        root = root.left
        height += 1
    return height

def find_right_height(root):
    height = 0
    while root.right:
        root = root.right
        height += 1
    return height

def count_nodes(root):
    if not root:
        return 0
    left = find_left_height(root)
    right = find_right_height(root)

    if left == right:
        return (2 << left) - 1
    else:
        return count_nodes(root.left) + count_nodes(root.right) + 1