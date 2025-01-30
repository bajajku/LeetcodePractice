class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # memo = {}
        # def function(i):
            
        #     if(i in memo):
        #         return memo[i]
        #     if(i >= len(nums) -1):
        #         memo[i] = 0
        #         return 0
            
        #     minI = float("inf")
        #     for j in range(1, nums[i] + 1):

        #         minI = min(minI, 1 + function(i + j))
            
        #     memo[i] = minI
        #     return minI
        # return(function(0))

        memo = [0] * len(nums)

        for i in range(len(nums)-2, -1, -1):
            minI = float("inf")
            for j in range(1, nums[i] + 1):
                val = float("inf")
                if(i + j <= len(nums) -1):
                    val = 1 + memo[i + j]
                minI = min(minI, val)
            memo[i] = minI
        return memo[0]



