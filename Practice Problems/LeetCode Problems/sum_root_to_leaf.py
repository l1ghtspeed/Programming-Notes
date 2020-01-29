# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        q = deque([(root, '')])
        paths = []
        while q:
            node, path = q.popleft()
            path += str(node.val)
            if not node.left and not node.right:
                paths.append(path)
            if node.left:
                q.append((node.left, path))
            if node.right:
                q.append((node.right, path))
        ans = 0
        for path in paths:
            for i, char in enumerate(path):
                ans += 2**(len(path)-1-i) * int(char)
        return ans
