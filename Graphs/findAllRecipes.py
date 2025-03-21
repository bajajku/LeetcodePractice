class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        hm = defaultdict(set)
        indegree = defaultdict(int)
        for i in range(len(ingredients)):
            igd = ingredients[i]
            indegree[recipes[i]] = len(igd)
            for x in igd:
                hm[x].add(recipes[i])

        q = []
        for s in supplies:
            q.append(s)
        q = deque(q)
        res = []
        while q:

            i = q.popleft()

            for p in hm[i]:
                indegree[p] -= 1

                if(indegree[p] == 0):
                    res.append(p)
                    q.append(p)

        
        return(res)
        

