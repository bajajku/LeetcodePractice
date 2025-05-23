class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        
        # 0111
        # 0011
        # 0100


        # 0001
        # 0011
        # 0010
        memo = {}
        def function(i, c):
            
            if (i, c) in memo:
                return memo[(i, c)]

            if i == len(nums):
                if c:
                    return 0
                return float("-inf")

            x = nums[i] ^ k
            pick = x + function(i + 1, not c)


            nPick = nums[i] + function(i + 1, c)

            memo[(i, c)] = max(pick, nPick)

            return max(pick, nPick)
        return function(0, True)
