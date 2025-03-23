class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:

        adjMat = [[] for _ in range(n)]

        for u, v, w in roads:
            adjMat[u].append((w, v))
            adjMat[v].append((w, u))

        
        MOD = 10**9 + 7

        minPath = [float("inf")] * n
        path_count = [0] * n
        path_count[0] = 1

        minHeap = [(0, 0)] # (weight, node)

        while minHeap:

            weight, node = heapq.heappop(minHeap)

            for nei_weight, nei in adjMat[node]:
                new_weight = weight + nei_weight

                if(new_weight < minPath[nei]):
                    path_count[nei] = path_count[node]
                    minPath[nei] = new_weight
                    heapq.heappush(minHeap, (new_weight, nei))

                elif(new_weight == minPath[nei]): 
                    path_count[nei] = (path_count[node] + path_count[nei]) % MOD

        return(path_count[-1])

