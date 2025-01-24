'''
First solution I can think of is kind of recursive as will try all combinations.

'''

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def function(stack, openN, closedN):

            if(openN == closedN == n):
                res.append("".join(stack[:]))
                return

            
            if(openN < n):
                _stack = stack[:]
                _stack.append("(")
                function(_stack, openN + 1, closedN)
            if(closedN < openN):
                _stack = stack[:]
                _stack.append(")")
                function(_stack, openN, closedN + 1)
        
        function([], 0, 0)

        return(res)

            
            
