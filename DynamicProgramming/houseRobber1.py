class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Recursive Approach
        """def function(index):

            if(index == 0):
                return nums[index]
            
            if(index < 0):
                return 0

            
            pick = nums[index] + function(index - 2)
            nPick = 0 + function(index - 1)

            return max(pick, nPick)
        
        return function(len(nums) -1)"""

        # Memoization

        """memo = [-1] * len(nums) 
        def function(index):

            if(index == 0):
                return nums[index]
            
            if(index < 0):
                return 0

            if(memo[index] != -1):
                return memo[index]
            
            pick = nums[index] + function(index -2)
            nPick = 0 + function(index -1)

            memo[index] = max(pick, nPick)
            return memo[index]

        return function(len(nums) -1)"""

        # Tabulation

        """memo = [-1] * (len(nums))
        memo[0] = nums[0]

        for index in range(1, len(nums)):

            pick = nums[index]
            if(index > 1):
                pick += memo[index - 2]
            nPick = memo[index - 1]

            memo[index] = max(pick, nPick)
        
        return memo[-1]"""

        # Space Optimized

        prev, prev2 = nums[0], 0 # prev: memo[i-1], prev2: memo[i-2]

        for index in range(1, len(nums)):

            pick = nums[index] + prev2

            nPick = prev

            prev2 = prev
            prev = max(pick, nPick)

        
        return prev

