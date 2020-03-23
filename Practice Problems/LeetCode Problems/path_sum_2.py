# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        ans, q = [], deque([(root, [], 0)])
        while q:
            node, path, s = q.popleft()
            if node.left:
                q.append((node.left, path + [node.val], s+node.val))
            if node.right:
                q.append((node.right, path + [node.val], s+node.val))
            if not node.right and not node.left and node.val + s == sum:
                ans.append(path + [node.val])
        return ans
        
