class ListNode(object):

    def __init__(self,x):
        self.val = x
        self.next = None


def reserve(head):

    curt = None
    while head != None:
        temp = head.next
        head.next = curt
        curt = head
        head = temp
        return curt

def printll(head):
    print()


n1 = ListNode(1)
n2 = ListNode(2)
n1.next = n2
