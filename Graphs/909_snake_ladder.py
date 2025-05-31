class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        
        n = len(board)
        flatten = [None] * ((n * n) + 1)

        d = True
        i = 1
        for r in range(n - 1, -1, -1):
            if d:
                for c in range(n):
                    flatten[i] = (r, c)
                    i += 1
            else:
                for c in range(n-1, -1, -1):
                    flatten[i] = (r, c)
                    i += 1
            
            d = not d
        
        
        visited = set()
        q = deque([1])
        visited.add(1)
        res = 0
        while q:
            
            qLen = len(q)
            for _ in range(qLen):
                node = q.popleft()
                if node == n * n:
                    return res

                for k in range(1, 7):

                    nextVal = node + k
                    if nextVal > n * n:
                        continue

                    r, c = flatten[nextVal]
                    if board[r][c] != -1:
                        nextVal = board[r][c]
                    
                    if nextVal in visited:
                        continue
                    visited.add(nextVal)
                    q.append(nextVal)
            
            res += 1

        return -1
