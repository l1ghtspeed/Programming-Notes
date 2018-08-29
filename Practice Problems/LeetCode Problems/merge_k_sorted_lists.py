# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import heapq

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = []
        output = []
        for root in lists:
            if root:
                heapq.heappush(heap, (root.val, root))
        while heap:
            node = heapq.heappop(heap)
            output.append(node[0])
            if node[1].next:
                heapq.heappush(heap, (node[1].next.val, node[1].next))
        return output
