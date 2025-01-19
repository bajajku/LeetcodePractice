class Solution(object):
    def countPalindromicSubsequence(self, s):
        """
        :type s: str
        :rtype: int
        """

        leftIndex = [float("inf")] * 26
        rightIndex = [float("-inf")] * 26

        res = 0

        for i in range(len(s)):

            leftIndex[ord(s[i]) - ord("a")] = min(leftIndex[ord(s[i]) - ord("a")], i)
            rightIndex[ord(s[i]) - ord("a")] = max(rightIndex[ord(s[i]) - ord("a")], i)

        print(leftIndex)
        print(rightIndex)

        for i in range(26):

            if(leftIndex[i] == float("inf") or rightIndex[i] == float("-inf") or leftIndex[i] == rightIndex[i] or rightIndex[i] - leftIndex[i] <= 1):
                continue

            a = s[leftIndex[i] + 1 : rightIndex[i]]
            x = len(set(a))

            res += x

        return(res)      

        




        
