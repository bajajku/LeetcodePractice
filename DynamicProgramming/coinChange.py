class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
        '''
        Recursive Approach:
        '''
        # def function(index, target):

        #     if(index == 0):
        #         if(target % coins[index] == 0):
        #             return target // coins[index]
        #         else:
        #             return float("inf")
            
        #     notTake = function(index - 1, target)
        #     take = float("inf")

        #     if(coins[index] <= target):
        #         take = 1 + function(index, target - coins[index])
            
        #     return min(take, notTake)
        
        # endCoinIndex = len(coins) -1
        # res = function(endCoinIndex, amount)

        # return res if res != float("inf") else -1

        '''
        Memoization solution:
        '''
        # dp = [[-1] * (amount + 1) for _ in range(len(coins))]
        # def function(index, target):

        #     if(index == 0):
        #         if(target % coins[index] == 0):
        #             return target // coins[index]
        #         else:
        #             return float("inf")
            
        #     if(dp[index][target] != -1):
        #         return dp[index][target]
            
        #     notTake = function(index - 1, target)
        #     take = float("inf")

        #     if(coins[index] <= target):
        #         take = 1 + function(index, target - coins[index])
            
        #     dp[index][target] = min(take, notTake)
        #     return min(take, notTake)
        
        # endCoinIndex = len(coins) -1
        # res = function(endCoinIndex, amount)

        # return res if res != float("inf") else -1

        '''
        Tabulation Solution
        '''
        dp = [[0] * (amount + 1) for _ in range(len(coins))]
        # Base Case:
            # For Index == 0, we will fill all possible targets(i.e 0 ... amount)

        for possTarget in range(amount + 1):
            if(possTarget % coins[0] == 0):
                dp[0][possTarget] = possTarget // coins[0]
            else:
                dp[0][possTarget] = float("inf")
        
        # travel all the possible states now starting from 1

        for index in range(1, len(coins)):
            for target in range(amount + 1):
                nTake = dp[index - 1][target]
                take = float("inf")
                if(coins[index] <= target):
                    take = 1 + dp[index][target-coins[index]]
                
                dp[index][target] = min(nTake, take)
        
        res = dp[-1][-1]

        return res if res != float("inf") else -1
 



        
