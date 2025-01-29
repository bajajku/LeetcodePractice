class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        n = len(edges)
        rank = [0 for i in range(n + 1)]
        par = [i for i in range(n + 1)]
        print(par)
        def find(u):

            if(u == par[u]):
                return u
            else:
                par[u] = find(par[u])
            
            return par[u]
        
        def union(u, v):

            ult_par_u = find(u)
            ult_par_v = find(v)

            if(ult_par_u == ult_par_v):
                return False

            elif(rank[ult_par_u] < rank[ult_par_v]):
                par[ult_par_u] = ult_par_v
                rank[ult_par_v] = ult_par_u
            else:
                par[ult_par_v] = ult_par_u
                rank[ult_par_u] = ult_par_v
        
        for u, v in edges:

            if(union(u,v) == False):
                return [u, v]
        
        return []

        
        
