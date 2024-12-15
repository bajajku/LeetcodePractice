'''
Classic Fibonnaci Problem: 0 1 1 2 3 ....

We identified the recurrence relation:
f(n) = f(n-1) + f(n - 2)

'''

class Solution:
    def climbStairs(self, n: int) -> int:

        # Recursive approach:
            # - TC = O(2^n)
            # - Space = O(n)

        '''
        def backtrack(i):

            if (i <= 1):
                return 1
            
            return backtrack(i - 1) + backtrack(i - 2)

        return backtrack(n)
        '''

        # Top Down Approach
            # - create a memo array
            # - convert return into memo call like memo[n] = ...
            # - TC = O(n)
            # - Space = O(n)
        '''
        memo = [-1] * (n + 1)
        def backtrack(i):

            if (i <= 1):
                return 1
            
            if memo[i] != -1:
                return memo[i]
            
            memo[i] = backtrack(i - 1) + backtrack(i - 2)
            return memo[i]

        return backtrack(n)
        '''

        # Bottom Up approach:
            # - create a memo array
            # - iteratively fill the memo array
            # - TC = O(n)
            # - Space = O(n)
        '''
        if n <= 2:
            return n
        memo = [0] * (n + 1)
        memo[1], memo[2] = 1, 2 # base cases

        for i in range(3, n + 1):
            memo[i] = memo[i-1] + memo[i-2]
        
        return memo[n]
        '''
        # Space Obtimized:
            # - Similar to bottom up, but we realized that at each step we are,
            # only using only 2 values, so why not use variables for that.
            # - example for f(5) we only need f(4) and f(3)
            # - TC = O(n)
            # - Space = O(1)
            
        if n <= 2:
            return n

        one = 1
        two = 2

        for i in range(3, n + 1):
            temp = one + two
            one = two
            two = temp
        
        return two

        
        
        
        


        