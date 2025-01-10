class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums) -1

        res = float("inf")

        # if left portion is sorted take the left element and deltet the lft part
        while l <= r:

            mid = (l+r) // 2

            if(nums[l] <= nums[mid]):
                res = min(res, nums[l])
                l = mid + 1
            else:
                res = min(res, nums[mid])
                r = mid - 1
        
        return res

        # if right part is sorted take the leftest element i. e mid of right half and elminate the right half
        
