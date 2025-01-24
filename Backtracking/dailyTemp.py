class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []
        res = [0] * len(temperatures) 

        for i in range(len(temperatures)):
            
            if(stack and temperatures[stack[-1]] >= temperatures[i]):
                stack.append(i)
            else:
                while(stack and temperatures[stack[-1]] < temperatures[i]):
                    out = stack.pop()
                    res[out] = i - out
            
            stack.append(i)
        
        return(res)


            
        
