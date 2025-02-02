class Solution:
    def checkValidString(self, s: str) -> bool:

        stack = []
        stars = []

        for i in range(len(s)):

            if(s[i] == "("):
                stack.append(i)
            elif(s[i] == "*"):
                stars.append(i)

            else:
                if(not stars and not stack):
                    return False
                if(stack):
                    stack.pop()
                elif(stars):
                    stars.pop()
        
        while stack and stars:
            if(stack.pop() > stars.pop()):
                return False
        
        return not stack



        
