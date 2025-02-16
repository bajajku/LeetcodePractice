class Solution:
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        
        totHeight = sum(maximumHeight)

        maximumHeight.sort()
        count = Counter(maximumHeight)

        if(1 in count):
            if count[1] > 1:
                return -1
        
        for h in maximumHeight:

            if(count[h] == 1):
                continue
            
            else:
                k = h
                k -= 1
                while k in count and k > 1:
                    k -= 1
                
                if(k in count):
                    return -1
                else:
                    totHeight = totHeight - (h - k)
                    count[h] -= 1
                    count[k] = 1
        
        return totHeight
                
                

