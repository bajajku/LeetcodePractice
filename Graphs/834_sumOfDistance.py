class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        
        mat = defaultdict(list)

        for u, v in edges:
            mat[u].append(v)
            mat[v].append(u)
        
        res = [0] * n
        count = [1] * n
        def dfs(node, par):

            for child in mat[node]:

                if child != par:
                    dfs(child, node)
                    count[node] += count[child]
                    res[node] += res[child] + count[child]
        
        def dfs_2(node, par):

            for child in mat[node]:
                if child != par:
                    res[child] = res[node] - count[child] + (n - count[child])
                    dfs_2(child, node)
        
        dfs(1, -1)
        dfs_2(1, -1)

        return res
                    

