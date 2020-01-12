# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        elems = []
        def collect_tree_elems(root):
            if root:
                collect_tree_elems(root.left)
                elems.append(root.val)      
                collect_tree_elems(root.right)
        collect_tree_elems(root)
        return elems[k-1]
        
