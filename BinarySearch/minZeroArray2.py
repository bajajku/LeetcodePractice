class Solution(object):
    def minZeroArray(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: int
        """
        def canZero(numQueries):
            prefix = 0
            diff_array = [0] * (len(nums) + 1)

            # populate difference array
            for query in range(numQueries):
                l, r, val = queries[query]
                diff_array[l] += val
                diff_array[r + 1] -= val # [r+1] to reverse the effects during prefix sum.
            
            # using prefix sum check if all zero is possible
            for numIdx in range(len(nums)):
                prefix += diff_array[numIdx]
                if(prefix < nums[numIdx]):
                    return False
                
            return True

        
        l, r = 0, len(queries)
        res = -1
        while l <= r:

            m = (l + r) // 2

            if(canZero(m)):
                res = m
                r = m - 1

            else:
                l = m + 1
        
        return res



        
