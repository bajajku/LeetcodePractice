class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        Prefix - Suffix method (more intuitional)
        '''
        # prefix = 1
        # suffix = 1
        # res = float("-inf")

        # for i in range(len(nums)):

        #     prefix *= nums[i]
        #     res = max(res, prefix)

        #     if(prefix == 0):
        #         prefix = 1
        
        # for j in range(len(nums)-1, -1, -1):

        #     suffix *= nums[j]
        #     res = max(res, suffix)

        #     if(suffix == 0):
        #         suffix = 1

        # return res

        '''
        a version of Kadane's Algorithm (almost like magic :) )
        '''
        
        
        res = nums[0]
        curMin = 1
        curMax = 1

        for i in range(len(nums)):
            
            num = nums[i]
            temp = curMax * num
            curMax = max(num * curMax, num * curMin, num)
            curMin = min(temp, num * curMin, num)

            res = max(res, curMax)

        return res

            

        
