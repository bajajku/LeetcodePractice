# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal):

        # if dashes are increasing, direct 
      '''
      Can be done using stack by trqacking the length of the stack,

      but in this we are using hashmap and dash variable to determine the level of node.
      Then iteratively doing bfs on whole string and connecting nodes.
      In end we construct a tree at hm[0] which is the root node.

      # Only edge case< numbers can be of len > 1, as "100" can be there 
      while dashes are individual.
      
      '''
            
        hm = {}
        i = 0

        c = ""
        while i < len(traversal) and traversal[i] != "-":
            c += traversal[i]
            i += 1
        hm[0] = TreeNode(val = int(c))

        dash = 0
        while i < len(traversal):
            char = traversal[i]
            if(char == "-"):
                dash += 1
                i += 1
            
            else:
                char = ""
                while i < len(traversal) and traversal[i] != "-":
                    char += traversal[i]
                    i += 1
                node = TreeNode(val = int(char))
                if(hm[dash -1].left == None):
                    hm[dash-1].left = node
                elif(hm[dash -1].right == None):
                    hm[dash-1].right = node
                
                hm[dash] = node

                dash = 0

        return(hm[0])
