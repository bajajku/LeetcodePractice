class Solution:

    '''
        we can pick 2 or 3 ele only
    
    '''
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)

        memo = [None] * n
        def function(i):

            if(i == len(nums)):
                return True
            
            if(memo[i] != None):
                return memo[i]
            
            r0 = False
            if(n - i >= 2):

                if(len(set(nums[i : i + 2])) == 1):
                    r0 = function(i + 2)
            
            r1 = False
            r2 = False
            if(n - i >= 3):
                if(len(set(nums[i : i + 3])) == 1):
                    r1 = function(i + 3)
                
                if(nums[i] + 2 == nums[i + 1] + 1 == nums[i + 2]):
                    r2 = function(i + 3)
            
            memo[i] = r1 or r2 or r0
            return r1 or r2 or r0

        
        return function(0)


                


        
