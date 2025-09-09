class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        

        # heights = [4,12,2,7,3,18,20,3,19], bricks = 10, ladders = 2

        # at each index we can go from brick or ladder
        
        # [idx, bricks, ladders]

        # brick_step = [[0, bricks, ladders]]
        # ladder_step = [[0, bricks, ladders]]

        pq = []
        for i in range(len(heights) - 1):

            cur = heights[i]
            nxt = heights[i + 1]

            if nxt <= cur:
                continue
            
            heapq.heappush(pq, nxt - cur)
            if len(pq) > ladders:
                bricks -= heapq.heappop(pq)
            
            if bricks < 0:
                return i
            
        return len(heights) - 1



