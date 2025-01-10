class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l, r = 0, 0
        res = 0

        MAP = {i: 0 for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}
        maxVal = 0
        while r < len(s):

            char = s[r]
            MAP[char] += 1

            maxVal = max(maxVal, MAP[char])
            while ((r - l + 1) - maxVal > k):
                MAP[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)

            r += 1
        
        return (res)

