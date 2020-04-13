from heapq import heapify, heappop, heapreplace


class ListNode(object):
    def __init__(self, x):
        self.next = None
        self.val = x
    pass


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        dummy = node = ListNode(0)
        h = [(n.val, n) for n in lists if n]
        heapify(h)
        while h:
            v, n = h[0]
            if n.next is None:
                heappop(h) #only change heap size when necessary
            else:
                heapreplace(h, (n.next.val, n.next))
            node.next = n
            node = node.next

        return dummy.next


list1 = ListNode(1)
list1.next = ListNode(3)
list2 = ListNode(2)
list2.next = ListNode(4)

Solution().mergeKLists([list1, list2])
