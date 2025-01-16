class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        maxArea = float("-inf")

        l, r = 0, len(height) -1

        while l < r:

            area = min(height[l], height[r]) * (r - l)

            maxArea = max(area, maxArea)

            if(height[l] <= height[r]):
                l += 1
            else:
                r -= 1
        
        return maxArea


        
