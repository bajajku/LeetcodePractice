class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        

        nums.sort()

        res = 0

        minVal = nums[0]

        for n in range(1, len(nums)):

            if(nums[n] - minVal) <= k:
                continue
            
            res += 1
            minVal = nums[n]
        
        return res + 1
