class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        
        def returnMax(k, nk, f, e, s):
            
            stack = []
            res = 0

            for i in range(len(s)-1, -1, -1):
                
                if s[i] == e:
                    if stack and stack[-1] == f:
                        res += k
                        stack.pop()
                        continue
                
                stack.append(s[i])
            
            newS = "".join(stack)[::-1]

            
            return res, newS

        res = 0
        if y > x:
            
            init, newS = returnMax(y, x, "a", "b", s)
            res += init

            second, _ = returnMax(x, y, "b", "a", newS)

            res += second
        
        else:
            init, newS = returnMax(x, y, "b", "a", s)
            res += init

            second, _ = returnMax(y, x, "a", "b", newS)

            res += second
        
        return(res)




