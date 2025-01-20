class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        if(len(t) > len(s)):
            return ""

        haveMap = {}
        needMap = {}

        

        res, resLen = "", float("inf")

        for t in t:
            if(t in needMap):
                needMap[t] += 1
            else:
                needMap[t] = 1
        
        have, need = 0, len(needMap)

        l, r = 0, 0

        while r < len(s):

            char = s[r]

            if(char in haveMap):
                haveMap[char] += 1
            else:
                haveMap[char] = 1

            if(char in needMap and haveMap[char] == needMap[char]):
                have += 1
            
            while have == need:
                potential_res, length = s[l: r + 1], r - l + 1

                if(length < resLen):
                    res = potential_res
                    resLen = length
                
                haveMap[s[l]] -= 1

                if(s[l] in needMap and haveMap[s[l]] < needMap[s[l]]):
                    have -= 1
                l += 1
            
            r += 1

        return res if resLen < float("inf") else ""
        

                




        
