def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        node1 = l1
        node2 = l2
        s1 = ''
        s2 = ''
        summ = 0
        while node1:
            s1 += str(node1.val)
            node1 = node1.next
        while node2:
            s2 += str(node2.val)
            node2 = node2.next
        if s1 and s2:
            summ = int(s1[::-1]) + int(s2[::-1])
            summS = str(summ)[::-1]
            n = []
            for c in summS:
                n.append(int(float(c)))
            return n
        else:
            return 0
