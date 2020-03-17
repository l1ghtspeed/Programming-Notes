class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        def recurse(n1, n2):
            if (n1 and n2 and n1.val != n2.val) or (n1 and not n2) or (n2 and not n1):
                return False
            return (not n1 and not n2) or (recurse(n1.left, n2.right) and recurse(n1.right, n2.left))
        return recurse(root.left, root.right)
