class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        graph = {i: [] for i in range(n)}

        for v, e in edges:
            graph[v].append(e)
            graph[e].append(v)

        numNode = 0

        q = deque([(0, -1)])

        while q and numNode < n + 1:

            node, par = q.popleft()
            numNode += 1

            for nei in graph[node]:
                if(nei == par):
                    continue
                
                q.append((nei, node))

        
        return numNode == n

                




