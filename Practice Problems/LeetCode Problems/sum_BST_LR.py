# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


from collections import deque

class Solution:
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        count = 0
        q = deque()
        q.append(root)
        while q:
            node = q.pop()
            if node.val <= R and node.val >= L:
                count += node.val
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        return count

 # A cleaner solution exists, although technically the big O run time is identical (worst case). 
    # The new solution makes use of the properties of a BST to make sure there is no traversal of unnecessary nodes.
    
    def cleanerSolution(self, root, L, R):
        ans = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                if L <= node.val <= R:
                    ans += node.val
                if L < node.val:
                    stack.append(node.left)
                if node.val < R:
                    stack.append(node.right)
        return ans