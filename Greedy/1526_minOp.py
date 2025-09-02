class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        
        res = target[0]
        for i in range(len(target) - 1):
            cur, nxt = target[i], target[i + 1]
            if nxt > cur:
                res += (nxt - cur)
        
        return res
