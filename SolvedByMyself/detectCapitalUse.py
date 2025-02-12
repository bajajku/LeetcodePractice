class Solution:
    def detectCapitalUse(self, word: str) -> bool:

        if(len(word) == 1):
            return True

        
        if word[0] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            if word[1] in "abcedfghijklmnopqrstuvwxyz":
                for w in range(2, len(word)):
                    if(word[w] not in "abcedfghijklmnopqrstuvwxyz"):
                        return False
            else:
                for w in range(2, len(word)):
                    if(word[w] not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
                        return False
        else:
            for w in range(len(word)):
                if(word[w] not in "abcedfghijklmnopqrstuvwxyz"):
                    return False


        return True


        
