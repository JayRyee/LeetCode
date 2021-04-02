# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        dummyHead = ListNode()
        carry = 0
        p = l1
        q = l2
        curr = dummyHead

        while p is not None or q is not None:
            if p is None:
                x = 0
            else:
                x = int(p.val)

            if q is None:
                y = 0
            else:
                y = int(q.val)

            sum = carry + x + y

            carry = int(sum/10)

            curr.next = ListNode(int(sum % 10))
            curr = curr.next

            if p is not None:
                p = p.next

            if q is not None:
                q = q.next

        if (carry >= 1):
            curr.next = ListNode(carry)

        return dummyHead.next
