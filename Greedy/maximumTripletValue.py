class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:

        # maxi = nums[0]
        # res = 0
        # for j in range(1, len(nums) -1):
        #     for k in range(j + 1, len(nums)):
        #         res = max(res, (maxi - nums[j]) * nums[k])

        #     maxi = max(maxi, nums[j])
        
        # return res


        maxElement, maxDiff, res = 0, 0, 0

        for n in nums:
            res = max(res, maxDiff * n)
            maxDiff = max(maxDiff, maxElement - n)
            maxElement = max(maxElement, n)

            # print("res = ", res)
            # print("maxDiff = ", maxDiff)
            # print("maxEle = ", maxElement)
            # print()

        return res
            

        
