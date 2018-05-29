## Trees

### General Terminology

A tree is either empty, or a node with child nodes that are also trees (recursive)

*Ancester*: a node's ancestors are their parent node and parent of parent nodes

*Descendant*: a node's descendants are all of their child nodes and children of child nodes

*Root*: The top most node, is an ancestor of all other nodes in the tree and also all other node's are descendants of the root node

*Siblings*: Nodes that share the same parent nodes - would also have the same ancesters

*Leaf*: Node with no child nodes (bottom of tree)

*Interior Nodes*: Non-leaves, has child nodes

*Level*: A node's level is 1 + number of edges to the root node (can also think of as number of ancestors)

*Height*: A node's height is 1 + number of branches until lowest descendant leaf (kind of opposite of level)

*Forest*: A collection of trees

A node contains: a key, list containing some number of child nodes (can be 0), and a parent (unless it's the root node)

*Walking a Tree*: Traversing through the nodes of a tree in a particular order

*Breadth First Traversal*: Traversing by going through all the nodes in the same level before moving on to all the nodes in the next level. Can be implemented using Queues

*Depth First Traversal*: Traversing by going down all the descendants before moving on to sibling nodes. Can be implemented using Stacks

Ordering for Possible Depth First Search Traversal:

*In Order Traversal*: Left node, parent node, right node

*Pre Order Traversal*: Parent node, left node, right node

*Post Order Traversal*: Left node, right node, parent node

### Types of Trees

There's literally like a million different types of trees, but most commonly used tree structures can be split into four subcategories:

    1. Binary Trees - trees in which every node has at most two child nodes. Examples (Binary search tree, AVL trees, Red-black trees)

    2. Heaps - trees in which the parent node always contains a value that is greater than that of it's child nodes.

    3. Multi Branch Trees - trees in which any node can have any number of child nodes.

Trees are very flexible data structure in which their type and implementation can vary greatly depending on the question or problem they are used to solve.



