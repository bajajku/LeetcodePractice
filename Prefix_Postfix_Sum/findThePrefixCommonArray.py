class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        
        res = []

        hs = set()

        i = 0

        while i < len(A):
            x = 0
            if(A[i] != B[i]):
                if(A[i] in hs):
                    x += 1
                if(B[i] in hs):
                    x += 1
            else:
                x += 1
            
            prefix = res[i - 1] if i > 0 else 0
            res.append(prefix + x)

            hs.add(A[i])
            hs.add(B[i])
            i += 1
        
        return res


        
