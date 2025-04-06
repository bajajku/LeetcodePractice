class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        
        # define a search space

        l, r = 1, maxSum # maxSum for now should change later.

        # define the check function
        def get_sum(mid, length):
            if mid > length:
                return (length * (2 * mid - length - 1)) // 2
            else:
                return ((mid - 1) * mid) // 2 + (length - (mid - 1))

        def check(mid):
            left = index
            right = n - index - 1
            leftSum = get_sum(mid, left)
            rightSum = get_sum(mid, right)
            total = leftSum + rightSum + mid  # include the peak
            return total <= maxSum



        k = 0
        while l <= r:

            mid = (l + r) // 2

            if(check(mid)):
                k = mid
                l = mid + 1
                # do something
            else:
                r = mid -1
                # do something

        return k
        
        
