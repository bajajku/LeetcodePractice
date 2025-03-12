class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

      '''
      upper bound: First index where element is greater than target,
      always initialize answer with last index
      '''
        l, r = 0, len(nums) -1
        target = 0
        ans = len(nums)
        while l <= r:

            m = (l + r) // 2
            if(nums[m] > target):
                ans = m
                r = m - 1
            else:
                l = m + 1

        posCount = len(nums) - ans
        ans = len(nums)
        l, r = 0, len(nums) -1

      '''
      lower bound: First index where element is greater than equal to target
      always initialize answer with last index
      '''

        while l <= r:

            m = (l + r) // 2
            if(nums[m] >= target):
                ans = m
                r = m - 1
            else:
                l = m + 1

        negCount = ans

        return max(negCount, posCount)




            


        
