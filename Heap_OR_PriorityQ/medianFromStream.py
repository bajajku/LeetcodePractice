class MedianFinder(object):

    def __init__(self):
        self.small = [] # saving the largest elements(minHeap)
        self.large = [] # sving smaller elements * -1 to emulate (maxHeap).
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        heapq.heappush(self.small, num * -1)

        if(self.small and self.large and self.small[0] * -1 > self.large[0]):
            heapq.heappush(self.large, heapq.heappop(self.small) * -1)

        # after these operations we might have uneven heaps
        # to mantain order

        if(len(self.small) > len(self.large) + 1):
            heapq.heappush(self.large, heapq.heappop(self.small) * -1)

        if(len(self.large) > len(self.small) + 1):
            heapq.heappush(self.small, heapq.heappop(self.large) * -1)        

    def findMedian(self):
        """
        :rtype: float
        """
        

        if(len(self.small) > len(self.large)):
            return self.small[0] * -1

        if(len(self.large) > len(self.small)):
            return self.large[0]
        
        return(((self.small[0] * -1) + self.large[0]) / 2.0)
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
