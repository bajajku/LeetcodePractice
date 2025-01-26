# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        def mergeTwoLists(list1, list2):

            if(list1 and not list2):
                return list1
            if(list2 and not list1):
                return list2

            if(not list1 and not list2):
                return None
            

            dummyNode = ListNode()
            cur = dummyNode
            while list1 and list2:
                if(list1.val <= list2.val):
                    cur.next = list1
                    list1 = list1.next
                else:
                    cur.next = list2
                    list2 = list2.next
                
                cur = cur.next
            
            if(list1):
                cur.next = list1
            elif(list2):
                cur.next = list2

            return dummyNode.next

        if not lists or len(lists) == 0:
            return None

        mergeLists = lists

        while len(mergeLists) > 1:
            tempList = []
            for i in range(0, len(mergeLists), 2):
                list1 = mergeLists[i]
                list2 = mergeLists[i +1] if (i + 1) < len(mergeLists) else None

                merged = mergeTwoLists(list1, list2)

                tempList.append(merged)
            
            mergeLists = tempList
        
        return mergeLists[0]


        




        
