class Solution:
    def clearDigits(self, s: str) -> str:

        stack = []

        for i in s:
            if i in "1234567890":
                if(stack):
                    stack.pop()
                else:
                    continue
            else:
                stack.append(i)
        
        return "".join(stack)
