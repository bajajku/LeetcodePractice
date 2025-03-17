class Solution:
    def clearStars(self, s: str) -> str:
        heap = []
        for i in range(len(s)):

            if s[i] != "*":
                ordC = ord(s[i]) - ord("a")
                he = (ordC, -i, s[i])
                heapq.heappush(heap, he)
            else:
                ord_c, idx, c = heapq.heappop(heap)

        heap.sort(key = lambda x: -x[1])
        
        res = ""
        for he in heap:
            res += he[2]
        
        return res
