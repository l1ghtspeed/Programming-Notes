'''
Problem:

Given k sorted singly linked lists, write a function to merge all the lists into one sorted singly linked list

'''

import heapq

def solve(l){
    # assume l is an array with the head nodes of all linked lists
    hq = []

    # assume there is a linkedlist class
    newList = linkedlist()
    for i in range(len(l)):
        heapq.heappush((l[i].value, i, l[i]))
    
    # while there are elements in heapque, keep popping out lowest value, replacing it when appropriate
    newListNode = newList.head
    while hq:
        node = heapq.heappop()
        if l[node[1]].next:
            l[node[1]] = l[node[1]].next
            hq.heappush((l[node[1]].value, node[1], l[node[1]]))
        newListNode.next = node[2]
        newListNode = newListNode.next
    return newList
}