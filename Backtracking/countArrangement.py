class Solution:
    def countArrangement(self, n: int) -> int:

        res = [0]

        candidates = [i for i in range(1, n + 1)]


        def function(choices, permI):

            if(permI == n + 1):
                res[0] += 1
                return

            for i in range(len(choices)):
                num = choices[i]
                if(num % permI == 0 or permI % num == 0):
                    _choices = choices[:i] + choices[i+1:]
                    permI += 1
                    function(_choices, permI)
                    permI -= 1

            
        function(candidates, 1)
        return(res[0])






            
        
