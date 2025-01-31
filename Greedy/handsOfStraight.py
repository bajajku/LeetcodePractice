class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
        if(len(hand) % groupSize != 0):
            return False

        countMap = Counter(hand)

        minHeap = []

        # we need to make minHeap with num and its counter
        for key, val in countMap.items():
            heapq.heappush(minHeap, key)
        
        while minHeap:

            k = heapq.heappop(minHeap)

            if(countMap[k] > 0):

                for i in range(k, k + groupSize):
                    if(countMap[i] > 0):
                        countMap[i] -= 1
                    else:
                        return False
            if(countMap[k] > 0):
                heapq.heappush(minHeap, k)
            
        return True
        # hand.sort()
        # countMap = Counter(hand)

        # for num in hand:
        #     if(countMap[num] > 0):
        #         for i in range(num, num + groupSize):
        #             if(countMap[i] > 0):
        #                 countMap[i] -= 1
        #             else:
        #                 return False
        
        # return True
        
