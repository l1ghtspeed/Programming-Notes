''' 

Problem Description:

This problem was asked by Amazon.

Given a node in a binary tree, return the next bigger element, also known as the inorder successor.

For example, the inorder successor of 22 is 30.

   10
  /  \
 5    30
     /  \
   22    35
You can assume each node has a parent pointer.

'''

'''

class Node:
    def __init__():
        self.val = 0
        self.left = None
        self.right = None
        self.parent = None

'''

from collections import deque

def solve(node):
    returnVal = None
    q = deque()
    # if node has a right child, perform in order traversal
    if node.right:
        q.append(node.right)
        while q:
            temp = q.pop()
            returnVal = temp.val
            q.append(temp.left)
        return returnVal

    # considering it is a leaf or only has left children, if it is the root node then there is nothing bigger
    if not node.parent:
        return None
    
    # if the current node is also a left child then the next biggest will just be it's parent
    if node.parent.val > node.val: 
        return node.parent.val

    # trickier if node passed is right child - we can solve this by keeping iterating up until it becomes a left child or until the root is reached, in which case there is no larger value
    q.append(node.parent)
    while q:
        temp = q.pop()
        if not temp.parent:
            return None
        if temp.parent.val > temp.val: 
            return temp.parent.val
        q.append(temp.parent)






    