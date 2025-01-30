class Solution:
    def canJump(self, nums):


        target = len(nums) -1
        for i in range(len(nums) -2, -1, -1):

            if(nums[i] + i >= target):
                target = i
        
        if target == 0:
            return True
        
        return False

        # dp = [-1] * len(nums)

        # def function(index):

        #     if(index == len(nums) - 1):
        #         return 1
            
        #     if(index < len(nums) and nums[index] == 0):
        #         dp[index] = 0
        #         return 0

        #     if(dp[index] != -1):
        #         return dp[index]
            
        #     for i in range(1, nums[index] + 1):

        #         if(function(index + i)):
        #             dp[index] = 1
        #             return 1
        #     dp[index] = 0
        #     return 0
            
        # res = function(0)

        # if(res == 0):
        #     return False
        # return True

