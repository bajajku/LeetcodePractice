''' Hard intuition but les go through it:

1) If sum(gas) < sum(cost), we cannot have enough gas to do a round return -1

2) Else we guaranteed have a solution, 
->now what makes a index invalid ?
If it decreases the sum to be negative

Why greedy? 

As at step 2 we know there is a guaranteed solution, so we just greedily eliminating options,
instead of finding the answer.
And if an option is considered till the end of the list then it is the solution cause question says "a unique solution."
'''

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        if(sum(gas) < sum(cost)):
            return -1

        total = 0
        res = 0
        for i in range(len(gas)):

            total += (gas[i] - cost[i])

            if total < 0:
                total = 0
                res = i + 1
        
        return res
            
