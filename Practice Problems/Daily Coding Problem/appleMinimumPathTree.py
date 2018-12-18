'''
Problem Description:

This question was asked by Apple.

Given a binary tree, find a minimum path sum from root to a leaf. With only positive values

For example, the minimum path in this tree is [10, 5, 1, 1], which has sum 17.

  10
 /  \
5    5
 \     \
   3    1
       /
      1 


Idea for solving the problem: use dijkstras


Problem Part Two:

Given a binary tree, find a minimum path sum from root to a leaf. With both positive and negative values

For example, the minimum path in this tree is [10, 5, 1, -1], which has sum 15.

  10
 /  \
5    5
 \     \
   2    1
       /
     -1 

Can no longer use dijkstras because of the negative values - use structural induction (kinda like bottom up from the leaves with recursion)

We pick the smallest value from the two child nodes at each step

'''
import heapq

def solve(root):
    q = [(root, root.val)]
    while q:
        node = q.heappop()
        if node.left:
            q.heappush((node.left, node[1]+node.left.val))
        if node.right:
            q.heappush((node.right, node[1]+node.right.val))
        
        if not node.left and not node.right:
           return node[1] 



class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.parent = None
        self.val = 0



def solve2(node):
    if node:
        left_size = solve2(node.left)
        right_size = solve2(node.right)
        return min(left_size, right_size) + node.val
    return 0