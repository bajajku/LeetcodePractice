# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        dp = {}
        def dfs(node, canRob):
            
                        
            if (node, canRob) in dp:
                return dp[(node, canRob)]
            if not node:
                return 0
            
            pick = 0
            nPick = 0
            if canRob:
                pick = node.val + dfs(node.left, False) + dfs(node.right, False)
                nPick = dfs(node.left, True) + dfs(node.right, True)
            else:
                nPick = dfs(node.left, True) + dfs(node.right, True)
            
            dp[(node, canRob)] = max(pick, nPick)
            return max(pick, nPick)
        
        return dfs(root, True)

        
    

                    

        
