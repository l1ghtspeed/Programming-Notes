'''
Problem Description:

Typically, an implementation of in-order traversal of a binary tree has O(h) 
space complexity, where h is the height of the tree. 
Write a program to compute the in-order traversal of a binary tree 
using O(1) space

'''

def in_order_traversal(root):
    curr = root

    while curr:
        if not curr.left:
            print curr.data
            curr = curr.right

        else:
            # Find the rightmost descendant of the left child.
            desc = curr.left
            while desc.right and curr != desc.right:
                desc = desc.right

            # Make it point to the current node.
            if not desc.right:
                desc.right = curr
                curr = curr.left

            # If the rightmost descendant already points to the current node,
            # revert the changes we made to the tree and print the node's value.
            else:
                desc.right = None
                print curr.data
                curr = curr.right