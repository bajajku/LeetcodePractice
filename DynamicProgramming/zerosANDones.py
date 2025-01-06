class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """

      '''
      Only feedback for me: Leave the python before python leaves you
      
      '''

        memo = [[[-1] * (n+1) for _ in range(m + 1)] for _ in range(len(strs))]
        # def function(index, zero , one):

        #     if index == 0:
        #         temp_zero = zero
        #         temp_one = one
        #         for i in strs[0]:
        #             if i == "1":
        #                 temp_one -= 1
        #             else:
        #                 temp_zero -= 1
        #         if temp_zero >= 0 and temp_one >= 0:
        #             return 1
        #         return 0

        #     if(memo[index][zero][one] != -1):
        #         return memo[index][zero][one]


        #     s = strs[index]
        #     nPick = function(index - 1, zero, one)

        #     pick = 0
        #     temp_zero = zero
        #     temp_one = one
        #     for i in s:
        #         if(i == "1"):
        #             temp_one -= 1
        #         else:
        #             temp_zero -= 1
        #     if(temp_zero >= 0 and temp_one >= 0):
        #         pick = 1 + function(index-1, temp_zero, temp_one)

        #     memo[index][zero][one] = max(pick, nPick)
        #     return max(pick, nPick)
        
        # return function(len(strs) -1, m, n)

        memo = [[[0] * (n+1) for _ in range(m + 1)] for _ in range(len(strs))]

        count_zero = 0
        count_one = 0
        for i in strs[0]:
            if i == "1":
                count_one += 1
            else:
                count_zero += 1             
        for zero in range(m + 1):
            for one in range(n + 1):
                temp_zero = zero - count_zero
                temp_one = one - count_one
                if(temp_zero >= 0 and temp_one>=0):
                    memo[0][zero][one] = 1
        
        for i in range(1, len(strs)):
            for z in range(m + 1):
                for o in range(n + 1):
                    s = strs[i]
                    nPick = memo[i-1][z][o]
                    pick = 0
                    temp_zero = z
                    temp_one = o
                    for j in s:
                        if(j == "1"):
                            temp_one -= 1
                        else:
                            temp_zero -= 1
                    if(temp_zero >= 0 and temp_one >= 0):
                        pick = 1 + memo[i-1][temp_zero][temp_one]
                    
                    memo[i][z][o] = max(nPick, pick)
        
        return(memo[-1][-1][-1])

        
