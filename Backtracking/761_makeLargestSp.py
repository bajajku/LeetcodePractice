class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        

        '''
        "(()(()))"

        "101101001100"

        "() (()()) (())"
        
        "10 110100 1100"

        "10 111000 1100"
        '''

        def backtrack(string):

            count = 0
            i = 0

            res = []

            for j, v in enumerate(string):
                count = count + 1 if v=='1' else count - 1

                if count == 0:
                    res.append('1' + backtrack(string[i + 1:j]) + '0')
                    i = j + 1
            
            return ''.join(sorted(res)[::-1])
        
        return backtrack(s)


        
