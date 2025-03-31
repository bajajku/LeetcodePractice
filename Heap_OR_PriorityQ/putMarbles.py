class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:

        splits_max = []
        splits_min = []

        for w in range(len(weights) -1):
            w1, w2 = weights[w], weights[w + 1]
            wei = (w1 + w2)
            splits_min.append(wei)
            splits_max.append(-wei)

        heapq.heapify(splits_min)
        heapq.heapify(splits_max)
        max_score = 0
        min_score = 0
        for i in range(k - 1):
            max_score += -(heapq.heappop(splits_max))
            min_score += heapq.heappop(splits_min)
        
        return (max_score - min_score)
    

        '''
        2 9 8 2 1 4

        2 and 4 will be inclued in every split regardless.

        now splits we can have is:
        -> 2 + 9 = 11
        -> 9 + 8 = 17
        -> 8 + 2 = 10
        -> 2 + 1 = 3
        -> 1 + 4 = 5

        lets say k = 3

        we must split like this :
        2 | 9 | 8 2 1 4

        max = 2 + 2 + 9 + 9 + 8 + 4 = 34

        2 9 8 2 | 1 | 4
        = 2 + 2 + 1 + 1 + 4 + 4 = 14


        (17 + 11) - (5 + 3) = 20,
        


        '''
        
