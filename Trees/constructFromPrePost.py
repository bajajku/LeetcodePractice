# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # preorder = M L R
        # postorder = L R M
        
        # preprocessing for faster retrieval
        postOrderHm = {val: i for i, val in enumerate(postorder)}

        if(preorder == [] or postorder == []):
            return None
        
        '''recognizing the pattern
          
            As this question is wuite ambiguous, there can be multiple trees with same pre and post,
            we can and left tree in preorder is constructed from child nodes in post: for ex
            
            preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]
            For left tree:
              preorder = [2, 4, 5], whereas postorder = [4, 2, 5]
            For right tree:
              preorder = [3, 6, 7] and postorder = [6, 7, 3]

            Recognizing this pattern we can recursively choose the index such that we can construct this tree
            that aims to follow this pattern.

            # This can only happen if or preorder len > 1 as next node starts the left tree.

        '''
        root = TreeNode(preorder[0])
        if(len(preorder) > 1):
            index = postOrderHm[preorder[1]]

            leftLen = len(postorder[:index + 1])

            root.left = self.constructFromPrePost(preorder[1: leftLen + 1], postorder[: index + 1])
            root.right = self.constructFromPrePost(preorder[leftLen + 1: ], postorder[index + 1:] )

        return root
