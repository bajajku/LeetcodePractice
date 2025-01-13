class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        def function(perms, choices):

            if(len(perms) == len(nums)):
                res.append(perms[:])
                return

            
            for i in range(len(choices)):
                perms.append(choices[i])
                newChoices = choices[:i] + choices[i+1:]
                function(perms, newChoices)

                perms.pop()
        
        function([], nums)

        return res

        
