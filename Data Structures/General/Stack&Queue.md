## Stacks

Can be implemented with either arrays or singular linked lists with head node (for O(n) runtime)

### Runtimes

Push - O(1): Add element to the back of array (or head of linked list)

Pop - O(1): Remove last element of array (or head of linked list)

Top - O(1): Return last element of array (or head of linked list)

isEmpty - O(1): Returns whether the counter is 0 or not


## Queues

Can be implemented with circular arrays or singular linked lists with head and tail node

### Runtimes

Enqueue - O(1): Add element to the tail pointer of array (or tail of linked list), move tail pointer up 1

Dequeue - O(1): Remove and return head pointer element of array (or head of linked list), move head pointer up 1

isEmpty - O(1): Returns whether the tail pointer and head pointer are equal