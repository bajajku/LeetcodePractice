class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # naive solution
        countMap = Counter(nums)

        maxHeap = []
        for key, val in countMap.items():
            heapq.heappush(maxHeap, (-val, key))
        
        res = []
        while k > 0:
           count, value = heapq.heappop(maxHeap)
           res.append(value)

           k -= 1
        
        return res

        '''
        Bucket Sort
        '''
        # countMap = Counter(nums)
        
        # MAP = {i: [] for i in range(len(nums) + 1)}

        # for key, val in countMap.items():

        #     MAP[val].append(key)
        # res = []
        # for val, count in reversed(list(MAP.items())):
        #     if MAP[val] != []:
        #         for i in MAP[val]:
        #             res.append(i)

        #             if(len(res) == k):
        #                 return res

        
