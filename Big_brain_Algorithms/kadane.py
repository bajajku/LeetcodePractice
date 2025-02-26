class Solution(object):
    def maxAbsoluteSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        '''
        So main intuition goes like this:
        -> we all know classic kadane to calculate max sum in subarray, 
        -> this question just have a slight twist, we can have smallest negative number when 
        absolute will become the max

        So, in this calculate max using classic kadane, and calculate min using reversed kadane
        
        '''

        # kadane's algorithm to find the max_subarray sum
        # calculate max, reset when num < 0

        res_max = 0
        n = 0

        for i in nums:
            n += i
            res_max = max(res_max, n)
            if(n < 0):
                n = 0
        
        # reversed kadane to find min_subarray sum
        # calculate min, reset when num > 0
        res_min = 0
        k = 0
        for i in nums:
            k += i
            res_min = min(res_min, k)
            if(k > 0):
                k = 0
        

        return max(res_max, abs(res_min))
        
