class Solution:
    def isHappy(self, n: int) -> bool:
        
        visited = set()

        def calc_sum_of_square(n):
            res = 0
            while n > 0:
                res += ((n % 10) ** 2)
                n = n // 10
            return res

        while True:
            num = calc_sum_of_square(n)
            if(num == 1):
                return True
            elif(num in visited):
                return False
            visited.add(num)
            n = num

        
            
