class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:

        hm = {} # {prod: [(a1, b1), (a2,b2)]}

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                prod = nums[i] * nums[j]
                if(prod in hm):
                    hm[prod] += 1
                else:
                    hm[prod] = 1
        res = 0
        for k, val in hm.items():
            if(val >= 2):
                res += val * 4 * (val - 1)
        
        return(res)

        # 2 -> 8
        # 3 -> 24
        # 4 -> 48
