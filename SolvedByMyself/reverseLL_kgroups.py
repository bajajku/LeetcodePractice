# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        mergeLists = []

        cur = head
        

        canP = True

        while cur:
            temp = cur
            for i in range(k -1):
                if(cur):
                    cur = cur.next
                else:
                    canP = False
            
            if(not cur):
                canP = False
            
            if not canP:
                mergeLists.append(temp)
                break
            prev = None
            p = 0
            while temp and p < k:
                t = temp.next 
                temp.next = prev
                prev = temp
                temp = t
                p += 1
            
            mergeLists.append(prev)
            cur = t
        
        def mergeKListsDirectly(lists):
            # Handle the case of an empty input list
            if not lists:
                return None
            
            # Dummy node to build the merged list
            dummy = ListNode()
            current = dummy

            # Iterate through each list and append its nodes to the merged list
            for lst in lists:
                while lst:
                    current.next = lst
                    current = current.next
                    lst = lst.next

            return dummy.next

        res = mergeKListsDirectly(mergeLists)
        return res


        

