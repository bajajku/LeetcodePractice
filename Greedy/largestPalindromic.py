class Solution:
    def largestPalindromic(self, num: str) -> str:
        
        if(all(x == "0" for x in num)):
            return "0"

        count = Counter(num)
        allVals = list(count.keys())

        mid = 0

        midExist = False

        for possMid in allVals:
            if(count[possMid] % 2 != 0):
                midExist = True

                mid = max(mid, int(possMid))

                count[possMid] -= 1
                if(count[possMid] == 0):
                    count.pop(possMid)

        res = ""
        if midExist:
            res += str(mid)

        allVals = list(count.keys()) 
        allVals.sort()

        if(allVals == [] or allVals == ['0']):
            return res

        for val in allVals:
            valCount = val * (count[val] // 2)
            res = valCount + res + valCount

        return res

        
