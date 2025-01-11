# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
So the Idea is pretty simple merge 2 lists and keep on merging till only one list is left.
'''
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        def merge2List(list1, list2):
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
            if(list2):
                cur.next = list2
            
            return dummyNode.next

        if not lists or len(lists) == 0:
            return None
        
        while len(lists) > 1:

            mergedList = []

            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i + 1] if (i+1) < len(lists) else None

                mergedList.append(merge2List(list1, list2))
            lists = mergedList

        return lists[0]
        
            
