class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        
        def formula(x, c):
            return (x + 1) + ((c-1) // (x + 1)) * (x + 1)

        count = Counter(answers)

        res = 0

        for x, c in count.items():
            res += formula(x, c)
        
        return(res)
        
