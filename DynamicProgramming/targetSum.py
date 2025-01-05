'''
0/1 knapsack problem
We have to use all elements.
1) Express in terms of index
    function(index, target)
        if index is n, it means with n elements, return me num of targets we can form


'''
class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        x = len(nums)
        s = sum(nums)
        memo = [[-1] * ((2 * s) + 1) for _ in range(x)]
        def function(index, t):

            if(index ==  0):
                res = 0
                if(t - nums[0] == target):
                    res += 1
                if(t + nums[0] == target):
                    res += 1
                return res
            
            if(memo[index][t + s] != -1):
                return memo[index][t + s]

            plus = function(index - 1, t + nums[index])
            neg = function(index - 1, t - nums[index])

            memo[index][t + s] = plus + neg
            return plus + neg

        
        return(function(len(nums)-1, 0))
