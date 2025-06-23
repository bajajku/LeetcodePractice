class Solution:
    def kMirror(self, k: int, n: int) -> int:
        
        def isPalindrome_baseK(num, k):
            digit = list()
            while num:
                digit.append(num % k)
                num //= k
            return digit == digit[::-1]


        left, cnt, ans = 1, 0, 0

        while cnt < n:
            right = left * 10

            for op in [0, 1]:

                for i in range(left, right):
                    if cnt == n:
                        break
                    
                    combined = i
                    x = i // 10 if op == 0 else i
                    while x:
                        combined = combined * 10 + x % 10
                        x //= 10
                    
                    if isPalindrome_baseK(combined, k):
                        cnt += 1
                        ans += combined
            left = right
        
        return ans

