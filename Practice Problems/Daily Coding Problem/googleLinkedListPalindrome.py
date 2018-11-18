'''
Problem:

This problem was asked by Google.

For example, 1 -> 4 -> 3 -> 4 -> 1 returns true while 1 -> 4 returns false.

'''

# doubly linked implementation
def solve(l):
    leftToRight = l.head
    rightToLeft = l.tail
    while leftToRight.next and rightToLeft.previous:
        if (leftToRight.val == rightToLeft.val):
            if leftToRight.next == rightToLeft or leftToRight == rightToLeft:
                return True
            else:
                leftToRight = leftToRight.next
                rightToLeft = rightToLeft.previous
        else:
            return False  
    return True

class Node():
    def __init__(self):
        self.next = None
        self.previous = None
        self.val = None


class LinkedList():
    def __init__(self):
        self.tail = Node()
        self.head = Node()
        self.tail.previous = self.head
        self.head.next = self.tail

    def __str__(self):
        temp = self.head
        while temp.next != self.tail:
            temp = temp.next
            print(temp.val)
        return 'End of LinkedList'

sampleList = LinkedList()
sampleList.head.next = Node()
sampleList.head.next.val = 1
sampleList.head.next.previous = sampleList.head
sampleList.head.next.next = Node()
sampleList.head.next.next.val = 1
sampleList.head.next.next.previous = sampleList.head.next
sampleList.head.next.next.next = sampleList.tail
#sampleList.head.next.next.next.val = 2
#sampleList.head.next.next.next.previous = sampleList.head.next.next
#sampleList.head.next.next.next.next = sampleList.tail
sampleList.tail.previous = sampleList.head.next.next
print(solve(sampleList))