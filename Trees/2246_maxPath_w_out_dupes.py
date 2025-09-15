class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        # at each node sum of its 2 best if we split, but only max if we don't split.

        ls = list(s) # for O(1) access.
        hm = {i: [] for i in range(len(parent))}
        for i in range(1, len(parent)):

            hm[parent[i]].append(i)

        res = [0]

        def dfs(node):
            maxVal = 0
            cv = []
            for child in hm[node]:
                childVal = dfs(child)
                if ls[child] != ls[node]:
                    maxVal = max(childVal, maxVal)
                    cv.append(childVal)
            
            cv.sort(reverse = True)
            tempRes = 1
            for i in range(min(len(cv), 2)):
                tempRes += cv[i]

            res[0] = max(tempRes, res[0])
            return maxVal + 1
        
        dfs(0)
        return(res[0])


            

        
