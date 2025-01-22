class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        
        queue = deque()
        rows = len(isWater)
        cols = len(isWater[0])
        visited = set() 

        for r in range(rows):
            for c in range(cols):
                if(isWater[r][c] == 1):
                    queue.append((r, c))
                    isWater[r][c] = 0
                    visited.add((r, c))
                else:
                    isWater[r][c] = 1

        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def isValid(r, c):

            if(r < 0 or c < 0 or r == rows or c == cols or (r,c) in visited):
                return False
            return True
        
        while queue:
            size = len(queue)
            for i in range(size):

                r, c = queue.popleft()

                for dr, dc in directions:

                    nr, nc = r + dr, c + dc
                    if(isValid(nr, nc)):
                        isWater[nr][nc] += isWater[r][c]
                        visited.add((nr, nc))
                        queue.append((nr, nc))

        return(isWater)
