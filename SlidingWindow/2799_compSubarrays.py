class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        
        l, r = 0, 0
        totalCount = len(set(nums))
        
        count = defaultdict(int)
        temp = 0
        res = 0
        n = len(nums)
        while r < n:
            num = nums[r]

            if count[num] == 0:
                temp += 1
            count[num] += 1

            while temp == totalCount:
                res += (n - r)

                count[nums[l]] -= 1
                if(count[nums[l]] == 0):
                    temp -= 1
                l += 1
            
            r += 1
        
        return res


