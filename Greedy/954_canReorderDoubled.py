class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        
        '''
            i = 0
            arr[1] = 2 * arr[0] 

            i = 1
            arr[3] = 2 * arr[2]

            i = 2
            arr[5] = 2 * arr[4]

        So odd elements are equal to 2 * (their corresponding evens)

        '''

        count = Counter(arr)
        arr.sort()

        for n in arr:
            if n > 0:
                if count[n] == 0:
                    continue
                if(n * 2 in count and count[n * 2] != 0):
                    count[n] -= 1
                    count[n*2] -= 1

                else:
                    return False
            elif n < 0:
                if count[n] == 0:
                    continue
                if(n / 2 in count and count[n/2] != 0):
                    count[n] -= 1
                    count[n/2] -= 1
                else:
                    return False
            

        return True
