class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        
        
        def match(c1, c2):
            for c, val in c2.items():
                if c1[c] < val:
                    return False
            return True

        res = 0

        count_2 = Counter(word2)

        l, r = 0, 0

        count_1 = defaultdict(int)
        while r < len(word1):

            count_1[word1[r]] += 1

            while match(count_1, count_2) and l <= r:
                res += len(word1) - r
                count_1[word1[l]] -= 1
                if count_1[word1[l]] < count_2[word1[l]]:
                    l += 1
                    break
                l += 1


            
            r += 1
        
        return(res)

        

