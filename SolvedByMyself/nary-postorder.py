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

"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

'''
Iterative solution using stack

'''
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        
        # if not root:
        #     return []
        # res = []
        # def postTraversal(root):
        #     if(not root):
        #         return
            
        #     for child in root.children:

        #         postTraversal(child)
        #         res.append(child.val)
        
        # postTraversal(root)
        # res.append(root.val)
        # return(res)

        if(not root):
            return []

        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            res.append(node.val)

            for j in range(len(node.children)):
                    
                if(node.children[j]):
                    stack.append(node.children[j])
                
        
        return res[::-1]
            
