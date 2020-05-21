# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:

    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        if not head:
            return

        # find the mid point
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second half in-place
        pre, node = None, slow
        while node:
            pre, node.next, node = node, pre, node.next

        # Merge in-place; Note : the last node of "first" and "second" are the same
        first, second = head, pre
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next

        return head


first_node = ListNode(1)
first_node.next = ListNode(2)
first_node.next.next = ListNode(3)
first_node.next.next.next = ListNode(4)

print(Solution().reorderList(first_node))