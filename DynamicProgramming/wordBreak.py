class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # go from (0...n)
        wordSet = set(wordDict)

        memo = [None] * (len(s) + 1)

        def function(index):

            if(memo[index] != None):
                return memo[index]

            if(index == len(s)):
                return True
            
            for j in range(index, len(s)):
                if(s[index:j+1] in wordSet):
                    if(function(j+1)):
                        memo[index] = True
                        return True
            
            memo[index] = False
            return False
        
        res = function(0)
        return res
        # wordSet = set(wordDict)
        # n = len(s)
        
        # # dp[i] represents if s[:i] can be segmented
        # dp = [False] * (n + 1)
        # dp[0] = True  # Base case: empty string can be segmented
        
        # for i in range(1, n + 1):
        #     for j in range(i):
        #         # Check if s[j:i] is in wordSet and s[:j] can be segmented
        #         if dp[j] and s[j:i] in wordSet:
        #             dp[i] = True
        #             break  # No need to check further if True
        
        # return dp[n] 
