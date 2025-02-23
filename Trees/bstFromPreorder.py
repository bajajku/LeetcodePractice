# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: Optional[TreeNode]
        """
      '''
      1) We recognize all small elements are in left tree, and all big in right.
      2) Also first element is always root

      So we recursively used this strategy to construct the tree/
    
      '''

        if not preorder:
            return None
        
        root = TreeNode(preorder[0])

        if(len(preorder) > 1):
            i = 1
            while i < len(preorder) and preorder[i] < preorder[0]:
                i += 1
            
            root.left = self.bstFromPreorder(preorder[1: i])
            root.right = self.bstFromPreorder(preorder[i: ])

        return root
            


        
