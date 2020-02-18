# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        q = deque([(root, root.val)])
        while q:
            node, path = q.popleft()
            if not node.left and not node.right and path == sum:
                return True
            if node.left:
                q.append((node.left, path + node.left.val))
            if node.right:
                q.append((node.right, path + node.right.val))
        return False
