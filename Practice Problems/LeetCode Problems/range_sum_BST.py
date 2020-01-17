# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        elems = []
        def traverse_Bst(root):
            if not root:
                return
            if root.val >= L and root.val <= R:
                elems.append(root.val)
            traverse_Bst(root.left)
            traverse_Bst(root.right)
        traverse_Bst(root)
        return sum(elems)
            
