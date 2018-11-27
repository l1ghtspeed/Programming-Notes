'''
Problem:

Write a function that finds if there is a loop in a linked list, in O(N) time and O(N) space

'''

# n is the head node of the linked list
def loopFind(n):
    fast = n
    slow = n
    while (fast.next.next != null):
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True

    return False