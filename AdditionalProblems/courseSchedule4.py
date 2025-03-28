class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        courseMap = {i: set() for i in range(numCourses)}

        for p in prerequisites:
            courseMap[p[1]].add(p[0])
        
        memo = [[-1] * numCourses for _ in range(numCourses)]
        def dfs(i, j):

            if(i in courseMap[j]):
                memo[i][j] = 1
                return True
            
            if(memo[i][j] != -1):
                if(memo[i][j] == 1):
                    return True
                else:
                    return False
            
            for pre in courseMap[j]:
                
                if dfs(i, pre):

                    memo[i][pre] = 1

                    return True
            memo[i][j] = 0
            return False


        res = []
        visited = set()
        for pre, crs in queries:

            if((pre, crs) in visited or dfs(pre, crs)):
                res.append(True)
                visited.add((pre, crs))
            else:
                res.append(False)

        return res
