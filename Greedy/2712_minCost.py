class Solution:
    def minimumCost(self, s: str) -> int:
        
        n = len(s)
        res = 0

        for i in range(1, n):

            if s[i] != s[i - 1]:
                res += min(i, n - i)
        
        return res
