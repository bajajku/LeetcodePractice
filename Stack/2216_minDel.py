class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        
        stack = []
        res = 0
        for i in range(len(nums)):

            if len(stack) % 2 == 0:

                stack.append(nums[i])
            
            else:
                if stack[-1] == nums[i]:
                    res += 1
                    continue
                else:
                    stack.append(nums[i])

        if len(stack) % 2 == 0:
            return res
        else:
            return res +1
            

