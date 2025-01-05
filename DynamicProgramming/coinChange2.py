class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """        
        '''
        Recurrence Relation: Brute Force
        '''
        # def function(index, target):

        #     if(index == 0):
        #         if(target % coins[0] == 0):
        #             return 1
        #         else:
        #             return 0
            
        #     nTake = function(index -1, target)
        #     take = 0
        #     if(target >= coins[index]):
        #         take = function(index, target - coins[index])

        #     res = take + nTake

        #     return res
        
        # return(function(len(coins) -1, amount))

        '''
        Top Down: Memoization
        '''
        # memo = [[-1] * (amount + 1) for _ in range(len(coins))]
        # def function(index, target):

        #     if(index == 0):
        #         if(target % coins[0] == 0):
        #             return 1
        #         else:
        #             return 0
            
        #     if(memo[index][target] != -1):
        #         return memo[index][target]
            
        #     nTake = function(index -1, target)
        #     take = 0
        #     if(target >= coins[index]):
        #         take = function(index, target - coins[index])

        #     memo[index][target] = take + nTake

        #     return memo[index][target]
        
        # return(function(len(coins) -1, amount))


        # '''
        # Bottom Up - Tabulation
        # '''
        # memo = [[0] * (amount + 1) for _ in range(len(coins))]
        
        # for t in range(amount + 1):
        #     if(t % coins[0] == 0):
        #         memo[0][t] = 1

        # for i in range(1, len(coins)):
        #     for target in range(amount + 1):
        #         nTake = memo[i-1][target]
        #         take = 0
        #         if(target >= coins[i]):
        #             take = memo[i][target - coins[i]]
                
        #         memo[i][target] = (take + nTake)

        # return memo[-1][-1]

        '''
        Space Optimized
        '''
        memo = [0] * (amount + 1)
        temp = [0] * (amount + 1)

        for t in range(amount + 1):
            if(t % coins[0] == 0):
                memo[t] = 1

        for i in range(1, len(coins)):
            for target in range(amount + 1):

                nTake = memo[target]
                take = 0
                if(target >= coins[i]):
                    take = temp[target - coins[i]]

                temp[target] = (nTake +  take)

            memo = temp

        return memo[-1]          
        


