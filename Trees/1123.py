# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # hm = defaultdict(set) # node: ancestors(TreeNode)
        # hm[root] = {root}

        # q = deque([root])
        # nodes = []
        # while q:
        #     qLen = len(q)
        #     t = []
        #     for _ in range(qLen):
        #         node = q.popleft()
        #         t.append(node)
        #         nodes.append(node)

        #         if(node.left):
        #             q.append(node.left)
        #             hm[node.left] = hm[node] | {node.left}
        #         if(node.right):
        #             q.append(node.right)
        #             hm[node.right] = hm[node] | {node.right}

        # res = None
        
        # for n in nodes:
        #     x = 0
        #     for a in t:
        #         if n in hm[a]:
        #             x += 1
        #     if x == len(t):
        #         res = n

        # return(res)

        # dfs

        def dfs(root):

            if not root:
                return (0, None)

            left = dfs(root.left)
            right = dfs(root.right)

            if(left[0] > right[0]):
                return (left[0] + 1, left[1])

            if(right[0] > left[0]):
                return (right[0] + 1, right[1])
            
            return (right[0] + 1, root)

        return dfs(root)[1]
        



