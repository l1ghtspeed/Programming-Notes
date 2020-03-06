# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.ans = []
        def recurse(node):
            if not node:    return
            recurse(node.left)
            self.ans.append(node.val)
            recurse(node.right)
        recurse(root)
        return self.ans
