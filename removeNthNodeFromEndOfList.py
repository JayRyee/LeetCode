# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:



        dummy = ListNode(0)
        dummy.next = head

        left = dummy
        right = dummy

        for i in range(0, n+1):
            right = right.next

        while right is not None:
            left = left.next
            right = right.next

        temp = left.next
        left.next = temp.next

        return dummy.next
