class Solution(object):
    def wordSubsets(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: List[str]
        """
        
        words2_count = [0] * 26

        for word in words2:

            tempCount = [0] * 26

            for c in word:

                tempCount[ord(c) - ord("a")] += 1
            

            for i in range(26):
                words2_count[i] = max(words2_count[i], tempCount[i])
        
        res = []

        valid = [0] * 26
        
        for word in words1:

            tempCount = words2_count[:]

            for c in word:
                tempCount[ord(c) - ord("a")] -= 1 if tempCount[ord(c) - ord("a")] > 0 else 0
            
            
            if(tempCount == valid):
                res.append(word)


        return(res)
