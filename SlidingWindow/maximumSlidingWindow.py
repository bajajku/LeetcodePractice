class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        # Brute force
        # for i in range(len(nums) - k + 1):

        #     res.append(max(nums[i: i + k]))
        
        # return res

        # Optimized using deque

        q = deque() # monotonic decreasing queue

        l, r = 0, 0

        while r < len(nums):

            while q and nums[q[-1]] < nums[r]: # [-1, 2, 3], nums[r] = 5
                q.pop()
            # []
            q.append(r)

            # index out of bound
            if(l > q[0]):

                # pop the left most element as in this turn it has went out of our window.
                q.popleft()
            
            # this means we have processed all k elements for the specific window.
            if(r + 1 >= k):
                res.append(nums[q[0]])
                l += 1
            
            r += 1
        
        return res

                


    

        
