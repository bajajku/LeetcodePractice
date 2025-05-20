class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        prefix = [0] * (len(nums) + 1)

        for i, j in queries:
            prefix[i] -= 1
            prefix[j + 1] += 1

        t = 0 # 0
        for k in range(len(nums)):
            t += prefix[k]
            if nums[k] + t > 0:
                return False
        
        return True
            
