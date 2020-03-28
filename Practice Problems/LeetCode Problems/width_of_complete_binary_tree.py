class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root: return 0
        if not root.left: return 1
        count = 0
        while root.left:
            count += 1
            root = root.left
        return count*2
