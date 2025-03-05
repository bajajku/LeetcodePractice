"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


'''
Observations:

1) 1 : [2, 4] ..... 4: [1, 3]

Key takeaways:
Go deeper and deeper and fill the hashmap

'''

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """

        if not node:
            return None
        
        

        q = deque([node])

        hm = {}
        hm[node.val] = Node(node.val)

        while q:
            
            n = q.popleft()
            for nei in n.neighbors:
                if(nei.val not in hm):
                    hm[nei.val] = Node(nei.val)
                    q.append(nei)
                hm[n.val].neighbors.append(hm[nei.val])
        

        return hm[node.val]



        


        
'''
v = {}

cN = Node(1)
v = {1: []}

cN = Node(2)
v = {1:[], 2:[]}

v = {1: [], 2:[1]}

cN = Node(3)
v = {1:[], 2:[1], 3: []}

v = {1: [], 2: [1], 3: [2]}

cN = Node(4)
v = {1: [], 2:[1], 3:{2}, 4: []}

v = {1: [], 2:[1], 3:{2}, 4: [1, 3]}

v = {1: [2, 3], 2:[1, 3], 3:{2, 4}, 4: [1, 3]}






'''
        
