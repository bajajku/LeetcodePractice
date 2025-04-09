class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        
        # comp_nodes: [4, 1, 2]
        # total_nodes: [7]

        # wrong assumption
        # Res = (7 - 4) + (7 - 1) + (7 - 2) = 3 + 6 + 5 = 14

        # it should be total pairs - comp pairs

        adjMat = {i: [] for i in range(n)}
        for v1, v2 in edges:
            adjMat[v1].append(v2)
            adjMat[v2].append(v1)

        comp = [0] * n

        visited = set()

        def dfs(n, _id):

            visited.add(n)
            comp[_id] += 1

            for nei in adjMat[n]:
                if(nei not in visited):
                    dfs(nei, _id)
        
        
        comp_id = 0
        for i in range(n):
            if i not in visited:
                dfs(i, comp_id)
                comp_id += 1
        
        
        res = 0

        total_pairs = n * (n - 1) // 2
        comp_pairs = sum(c * (c-1) // 2 for c in comp)

        return total_pairs - comp_pairs


