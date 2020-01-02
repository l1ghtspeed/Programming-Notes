from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        levels = {}
        return sum(levels[self.traverse_tree(levels, root)])
    
    def traverse_tree(self, levels, root):
        q = deque([(root, 0)])
        max_level = 0
        while q:
            node, level = q.popleft()
            
            if node.left:
                q.append((node.left, level+1))
            
            if node.right:
                q.append((node.right, level+1))
            
            if level in levels:
                levels[level].append(node.val)
            else:
                levels[level] = [node.val]
            
            max_level = max(level, max_level)
        
        return max_level
