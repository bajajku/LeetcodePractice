class Solution(object):
    def numberOfAlternatingGroups(self, colors, k):
        """
        :type colors: List[int]
        :type k: int
        :rtype: int
        """
        cLen = len(colors)
        colors = colors + colors

        l, r = 0, 0

        lastColor = -1
        cur = 0
        res = 0
        while l < cLen and r < len(colors):

            if(lastColor == -1 or (colors[r] == 1 and lastColor == 0) or (colors[r] == 0 and lastColor == 1)):
                cur += 1
            else:
                l = r
                cur = 1

            if(cur == k):
                res += 1
                l += 1
                cur -= 1
            lastColor = colors[r]
            r += 1
        
        return(res)

        

        
