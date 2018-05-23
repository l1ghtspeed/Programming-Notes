## Linked Lists & Doubly Linked Lists

### Runtimes 

All runtimes are given for Doubly Linked Lists (they are much more efficient, but requires more memory)!


Insertions:

    PushFront O(1) - Adds a new node to the front of the linked list, as simple as setting the head to new element

    PushBack O(1) - Adds a new node to the back of the linked list, just connect the new node

    AddBefore O(1) - Inserts new node before another specified node, reattach pointers

    AddAfter O(1) - Inserts new node after another specified node, reattach pointers


Deletions:

    PopFront O(1) - Removes the front node, just disconnect the node from the list

    PopBack O(1) - Removes last node, just assign the next pointer of the second last node to null

    Erase O(n) - Finds the first node with the given value, and removes that node. Needs to traverse down list


Other:

    isEmpty O(1) - Check if list is empty, see if head pointer is tail, or null

    Find O(n) - Check if element is in list, needs to traverse down list




    
