'''
1) We want to make an edges array.
2) We have created indegree map as well


'''

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        # h -> e -> r -> n -> f
        graph = {c: [] for w in words for c in w}

        indegree = {c: 0 for c in graph}

        for i in range(len(words) - 1):
            w, w2 = i, i + 1

            word1 = words[w]
            word2 = words[w2]

            minLength = min(len(word1), len(word2))

            # Edge case where we have [hrf, hr], as minLen = 2 so this is case is impossible to converge.
            if len(word1) > len(word2) and word1[:minLength] == word2[:minLength]:
                return ""

            w1i, w2i = 0, 0

            while w1i < len(word1) and w2i < len(word2):
                if(word1[w1i] != word2[w2i]):
                    if(word2[w2i] not in graph[word1[w1i]]):
                        graph[word1[w1i]].append(word2[w2i])
                        indegree[word2[w2i]] += 1
                    break
                w1i += 1
                w2i += 1
        print(graph)
        print(indegree)
        res = ""

        q = []
        for k, val in indegree.items():
            if(val == 0):
                q.append(k)
        
        q = deque(q)

        while q:
            node = q.popleft()
            res += node

            for nei in graph[node]:
                indegree[nei] -= 1
                if(indegree[nei] == 0):
                    q.append(nei)
        
        return res if len(res) == len(indegree) else ""

        
        
        

                


        
