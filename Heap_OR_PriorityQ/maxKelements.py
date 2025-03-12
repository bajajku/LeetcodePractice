class Solution(object):
    def maxKelements(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        maxHeap = []

        for n in nums:
            maxHeap.append(-n)

        heapq.heapify(maxHeap)

        res = 0
        for _ in range(k):

            num = heapq.heappop(maxHeap)
            num = -num
            res += num
            
            newNum = math.ceil(num/3.0)
            heapq.heappush(maxHeap, -newNum)
        
        return int(res)

        
