class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
   
        res = []
        def function(index, ss):

            if(index < 0):
                res.append(ss[:])
                return
            
            nPick = function(index -1, ss)

            ss.append(nums[index])
            pick = function(index -1, ss)

            ss.pop()
        
        function(len(nums)-1, [])
        return(res)
        
