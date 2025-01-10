class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        if len(s1) > len(s2):
            return False

        l, r = 0, len(s1) -1

        mapS1 = {}
        mapS2 = {}

        for i in "abcdefghijklmnopqrstuvwxyz":
            mapS1[i] = 0
            mapS2[i] = 0
        
        for c in s1:
            mapS1[c] += 1
        
        for c in range(r + 1):
            mapS2[s2[c]] += 1

        print(mapS1)
        print(mapS2)

        while r < len(s2):

            if mapS1 == mapS2:
                return True

            mapS2[s2[l]] -= 1
            l += 1
            r += 1
            if(r < len(s2)):
                mapS2[s2[r]] += 1

        return False   

        
