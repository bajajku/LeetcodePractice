class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        nums = [1] + nums + [1]

        memo = [[-1] * (len(nums) + 2) for _ in range(len(nums) + 2)]
        def function(l, r):

            if(l > r):
                return 0
            if(memo[l][r] != -1):
                return memo[l][r]
            
            maxi = 0

            for i in range(l, r + 1):

                coins = nums[l -1] * nums[i] * nums[r + 1]

                coins += function(l, i-1) + function(i + 1, r)

                maxi = max(maxi, coins)
                memo[l][r] = maxi
            
            return maxi
        
        return function(1, len(nums) - 2)


            
