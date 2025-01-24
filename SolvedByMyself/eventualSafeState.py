class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        indegree = [0] * len(graph)
        for i in range(len(graph)):
            for vertex in graph[i]:
                indegree[i] += 1
        
        MAP = {i: [] for i in range(len(graph))}
        for i in range(len(graph)):
            for vertex in graph[i]:
                MAP[vertex].append(i)

        queue = deque()
        for i in range(len(indegree)):
            if(indegree[i] == 0):
                queue.append(i)
        
        safe_nodes = []

        while queue:
            node = queue.popleft()
            safe_nodes.append(node)

            for nei in MAP[node]:
                indegree[nei] -= 1
                if(indegree[nei] == 0):
                    queue.append(nei)
        
        safe_nodes.sort()
        return safe_nodes
        
