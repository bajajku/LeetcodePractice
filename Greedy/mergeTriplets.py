class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        # First intuition is trying all possible ways to achieve:
        # exponential time complexity/

        # greedy approach 

        '''what we need is two things from my understanding:

            -> All three positions need  target's positions.
            -> There need to be at least 1 less than target in that position.

Kind of correct but if one of the val in trip is higher that target we just continye bruhhhh
        
        '''

        res = set()

        for t in triplets:

            if(t[0] > target[0] or t[1] > target[1] or t[2] > target[2]):
                continue
            
            else:
                if(t[0] == target[0]):
                    res.add(0)
                
                if(t[1] == target[1]):
                    res.add(1)
                
                if(t[2] == target[2]):
                    res.add(2)
            
            if(len(res) == 3):
                return True

        if(len(res) == 3):
            return True
        else:
            return False

                






