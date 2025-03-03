# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        '''
            -> Each node can split, or not split

            If it splits we take sumL + sumR + node
            Else:
                we take node + max(sumL, sumR, 0)
        '''

        '''
        Notes:
        -> what are the possibilities:
            -> we can go left or we can go right, but we can only split once.
            -> so at each node we will return max value if this node does't split, that means
            choose leftMax or rightMax or 0 if both less than 0.
            -> But we will also calculate node.val + leftMax + rightMax, 
            what if they split at this node. we use this to update the result.
            
        '''
        res = [float("-inf")]

        def function(node):

            if(not node):
                return 0

            leftMax = max(function(node.left), 0)
            rightMax = max(function(node.right), 0)

            potRes = node.val + leftMax + rightMax
            res[0] = max(res[0], potRes)

            return node.val + max(leftMax, rightMax)
        
        function(root)

        return res[0]


        
