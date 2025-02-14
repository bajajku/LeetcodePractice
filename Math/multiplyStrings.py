class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        # two approaches either do carry multiplication like kids
        # construct numbers using hashmap
        hm = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}

        n1 = len(num1) -1
        k1 = 0
        for i in num1:
            if n1 < 0:
                break
            k1 += (hm[i] * (10 ** n1))
            n1 -= 1
        
        n2 = len(num2) -1
        k2 = 0
        for i in num2:
            if n2 < 0:
                break
            k2 += (hm[i] * (10 ** n2))
            n2 -= 1

        return str(k1 * k2)

        

            



