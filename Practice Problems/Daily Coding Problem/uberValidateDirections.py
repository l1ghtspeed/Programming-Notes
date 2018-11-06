'''

Problem:

This problem was asked by Uber.

A rule looks like this:

A NE B

This means this means point A is located northeast of point B.

A SW C

means that point A is southwest of C.

Given a list of rules, check if the sum of the rules validate. For example:

A N B
B NE C
C N A
does not validate, since A cannot be both north and south of C.

A NW B
A N B
is considered valid.

'''

'''

My Approach:

My approach is to create a grid type system using a dictionary where everytime a new node is called it's coordinates are either updated or checked for validity.

E.G.

A NE B

Then the dictionary will look like:

{
    A: (0, 0),
    B: (1, 1)
}

If two nodes that are called already exist, we can use math to figure out if it is correctly in position. 

''' 