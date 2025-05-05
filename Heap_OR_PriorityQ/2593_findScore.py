class Solution:
    def findScore(self, nums: List[int]) -> int:
        res = 0

        hm = {}

        minHeap = []

        for i in range(len(nums)):

            minHeap.append((nums[i], i))
            hm[i] = nums[i]
        
        heapq.heapify(minHeap)
        while minHeap:

            val, ind = heapq.heappop(minHeap)

            if(ind in hm):
                res += val
                hm.pop(ind)

                if(ind - 1 in hm):
                    hm.pop(ind-1)
                if(ind + 1 in hm):
                    hm.pop(ind + 1)
        
        return res

