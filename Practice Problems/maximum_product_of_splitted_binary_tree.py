# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        q = deque([root])
        arr = []
        def memoize(root):
            if root.left:
                root.val += memoize(root.left)
            if root.right:
                root.val += memoize(root.right)
            return root.val
        memoize(root)
        
        ans = 0
        while q:
            node = q.popleft()
            if node.left:
                new = (root.val - node.left.val) * node.left.val
                if ans < new:
                    ans = new
                q.append(node.left)
            if node.right:
                new = (root.val - node.right.val) * node.right.val
                if ans < new:
                    ans = new
                q.append(node.right)
        return ans%((10**9) + 7)
