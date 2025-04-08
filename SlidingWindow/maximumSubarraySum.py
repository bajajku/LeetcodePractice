class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        
        l, r = 0, 0

        hm = defaultdict(int)
        s = 0
        res = float("-inf")
        while r < len(nums):

            num = nums[r]
            hm[num] += 1
            s += num

            while hm[num] > 1:
                s -= nums[l]
                hm[nums[l]] -= 1
                l += 1
            
            if (r - l + 1 == k):
                res = max(res, s)
                s -= nums[l]
                hm[nums[l]] -= 1
                l += 1
            
            r += 1
            
        return res if res != float("-inf") else 0




            
