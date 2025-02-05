class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        # def fact(n):

        #     if(n == 0 or n == 1):
        #         return 1
            
        #     return n * fact(n -1)
        
        # total_comb = fact(n) // (fact(k) * (fact(n-k)))
        
        nums = [i for i in range(1, n + 1)]
        res = []
        def backtrack(combo, choices):

            if(len(combo) == k):
                res.append(combo[:])
                return

            for i in range(len(choices)):
                combo.append(choices[i])

                _choices = choices[i+1:]

                backtrack(combo, _choices)

                combo.pop()
        
        backtrack([], nums)
        return(res)

