# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        node = root
        n = None
        while node and node.val != p.val:
            if p.val < node.val:
                n = node
                node = node.left
            else:
                node = node.right
        
        if not node:
            return None
        
        if not node.right:
            return n
        
        node = node.right
        while(node.left!=None):
            node = node.left
        return node
