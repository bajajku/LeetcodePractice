class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        heapq.heapify(nums)

        res = 0

        while nums:
            if(len(nums) == 1 and nums[0] >= k):
                return res
                
            n1 = heapq.heappop(nums)
            
            n2 = heapq.heappop(nums)
            
            if(n1 >= k and n2 >= k):
                return res
            
            val = min(n1, n2) * 2 + (max(n1, n2))

            heapq.heappush(nums, val)
            res += 1
