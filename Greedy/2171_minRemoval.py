class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        
        n = len(beans)
        beans.sort()

        lhs = [0] * n
        s = 0
        for b in range(len(beans)):

            if b > 0:
                lhs[b] = s
            
            s += beans[b]
        

        rhs = [0] * n
        s = 0
        for b in range(n -1, -1, -1):
            if b < n -1:
                rhs[b] = s - ((beans[b]) * (n - b - 1))
            
            s += beans[b]

        res = float("inf")
        for i in range(n):
            res = min(res, lhs[i] + rhs[i])
        
        return res
