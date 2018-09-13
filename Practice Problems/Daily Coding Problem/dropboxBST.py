def second_largest(root):
    def inorder(node):
        if not node or count[0] == 2:
            return

        if node.right:
            inorder(node.right)

        count[0] += 1
        if count[0] == 2:
            val.append(node.val)
            return

        if node.left:
            inorder(node.left)

    count = [0]
    val = []
    inorder(root)
    return val[0]