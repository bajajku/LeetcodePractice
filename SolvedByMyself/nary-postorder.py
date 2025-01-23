"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        
        if not root:
            return []
        res = []
        def postTraversal(root):
            if(not root):
                return
            
            for child in root.children:

                postTraversal(child)
                res.append(child.val)
        
        postTraversal(root)
        res.append(root.val)
        return(res)

            
