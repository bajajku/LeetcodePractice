class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        n = len(heights)

        lne = [-1] * n
        rne = [n] * n

        stack = []

        for i in range(n):

            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            
            if(stack):
                lne[i] = stack[-1]
            
            stack.append(i)
        
        stack = []

        for i in range(n-1, -1, -1):

            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            
            if(stack):
                rne[i] = stack[-1]
            
            stack.append(i)
        
        res = float("-inf")
        for i in range(len(heights)):
            area = heights[i] * (rne[i] - lne[i] - 1)
            res = max(res, area)

        return(res)
        



        
