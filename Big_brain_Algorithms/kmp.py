class Solution:
    def longestPrefix(self, s: str) -> str:
        
        if len(s) == 1:
            return ""

        kmp = [0] * len(s)
        l, r = 0, 1

        while r < len(s):

            if s[l] == s[r]:
                kmp[r] = l + 1
                l += 1
                r += 1

            elif l > 0:
                l = kmp[l - 1]
            else:
                r += 1
        
        return s[:kmp[-1]]
