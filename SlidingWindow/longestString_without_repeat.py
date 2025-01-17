class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        res = 0

        curLen = 0

        hs = set()

        l, r = 0, 0

        while l <= r and r < len(s):

            char = s[r]

            if(char not in hs):
                curLen += 1
                hs.add(char)
                r += 1
            else:
                res = max(res, curLen)
                while char in hs:
                    hs.remove(s[l])
                    l += 1
                    curLen -= 1
        
        return max(res, len(hs))

