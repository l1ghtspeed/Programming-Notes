'''

Problem:

Given the head of a singly linked list, reverse the list in place.

'''

def solve(head):
    curr = head
    prev = None

    while curr.next:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    
    return curr