# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """

        dummyNode = ListNode(next = head)

        slow = dummyNode
        fast = head

        while fast and n != 0:
            fast = fast.next
            n -= 1
        
        while slow and fast:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next

        return dummyNode.next
        
