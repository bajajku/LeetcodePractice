class Solution(object):
    def largestOverlap(self, img1, img2):
        """
        :type img1: List[List[int]]
        :type img2: List[List[int]]
        :rtype: int
        """
        
        image1 = []
        image2 = []
        n = len(img1)
        diff = {}


        for i in range(n):
            for j in range(n):

                if(img1[i][j] == 1):
                    image1.append((i, j))

                if(img2[i][j] == 1):
                    image2.append((i,j))
        
        res = 0
        for v1 in image1:
            for v2 in image2:
                
                d = (v1[0] - v2[0], v1[1] - v2[1])
                if(d not in diff):
                    diff[d] = 1
                else:
                    diff[d] += 1
                res = max(res, diff[d])

        return res


