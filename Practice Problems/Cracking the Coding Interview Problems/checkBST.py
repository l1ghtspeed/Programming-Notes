'''
Given a binary tree, check if it a bst.
'''

def solve(n, maxVal, minVal):
    # n is node, root node of tree is assumed to be passed in
    if not n:
        return True
    else:
        if n.val > maxVal or n.val < minVal:
            return False

        return solve(n.left, n.val, minVal) and solve(n.right, maxVal, n.val)
 


class Node():
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


root = Node(5)
root.left = Node(3)
root.right = Node(7)
root.left.right = Node(3)
root.left.left = Node(1)
root.right.right = Node(20)
root.right.left = Node(6)

print(solve(root, 20000000, -20000000))