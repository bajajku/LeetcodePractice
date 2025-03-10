class Solution(object):
    def countOfSubstrings(self, word, k):
        """
        :type word: str
        :type k: int
        :rtype: int
        """
        def atleastk(k):

            l, r = 0, 0

            vowels = defaultdict(int)
            cons = 0
            res = 0

            while r < len(word):
                
                w = word[r]
                if(w in "aeiou"):
                    vowels[w] += 1
                else:
                    cons += 1
                
                while(len(vowels) == 5 and cons >= k):
                    res += len(word) - r

                    if(word[l] in vowels):
                        vowels[word[l]] -= 1
                        if(vowels[word[l]] == 0):
                            vowels.pop(word[l])
                    else:
                        cons -= 1
                    l += 1

                    
                
                r += 1
            
            return res
        
        return atleastk(k) - atleastk(k+1)
