# Q814


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution:
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        # perform postorder traversal
        if not root:
            return None
        elif root.left and root.right:
            root.left = self.pruneTree(root.left)
            root.right = self.pruneTree(root.right)
            if root.left or root.right or root.val == 1:
                return root
            else:
                return None
        elif root.left:
            root.left = self.pruneTree(root.left)
            if root.left or root.val == 1:
                return root
            else:
                return None
        elif root.right:
            root.right = self.pruneTree(root.right)
            if root.right or root.val ==1:
                return root
            else:
                return None
        else:
            if root.val == 0:
                return None
            return root
    