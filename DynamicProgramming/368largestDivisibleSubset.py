class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        
        nums.sort()
        # res = []
        # def function(i, ss):
        #     nonlocal res
        #     if i >= len(nums):
        #         if len(ss) > len(res):
        #             res = ss[:]
        #         return

        #     if not ss or ss[-1] % nums[i] == 0 or nums[i] % ss[-1] == 0:
        #         pick = function(i + 1, ss + [nums[i]])
        #     nPick = function(i + 1, ss)

        # function(0, [])
        # return(res)

        dp = [[nums[i]] for i in range(len(nums))]

        for i in range(len(nums)): # 0 .. 3
            for j in range(i): # 0 .. i
                if(nums[i] % nums[j] == 0):
                    if len(dp[j]) + 1 > len(dp[i]):
                        dp[i] = dp[j] + [nums[i]]
        
        return max(dp, key = len)
