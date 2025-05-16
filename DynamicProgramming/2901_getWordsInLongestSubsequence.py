class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        
        def calculate_hamming(s1, s2):
            ham = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    ham += 1
                
                if ham > 1:
                    return False
            return ham == 1


        res = []

        hsh = [0] * len(words)
        dp = [1] * len(words)
        maxVal = float("-inf")
        maxIndex = -1

        for i in range(len(words)):
            hsh[i] = i
            for j in range(i):

                if groups[i] != groups[j] and len(words[i]) == len(words[j]) and calculate_hamming(words[i], words[j]):

                    if dp[i] < dp[j] + 1:
                        dp[i] = dp[j] + 1
                        hsh[i] = j
            
            if dp[i] >= maxVal:
                maxVal = dp[i]
                maxIndex = i
        
        res = []
        res.append(words[maxIndex])

        while hsh[maxIndex] != maxIndex:
            maxIndex = hsh[maxIndex]
            res.append(words[maxIndex])
        
        res = res[::-1]

        return res



