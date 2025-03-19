class Solution:
    def recoverArray(self, nums: List[int]) -> List[int]:
        
        '''
        Given:

        [122]
        
        
        '''

        

        def k_exist(k):
            count = Counter(nums)
            ans = []

            for num in nums:
                # if count of number == 0 then we mighve visited this number
                if(count[num] == 0):
                    continue

                # if count of num + k == 0, then this number doesnt exist, or we have used it before
                if(count[num + k] == 0):
                    break
                
                # decrement lower num count and higher num count
                count[num] -= 1
                count[num + k] -= 1

                # append the middle of lower and higher.
                ans.append(num + k // 2)
            
            # if we can form half of the array we are good
            if(len(ans) == len(nums) // 2):
                return ans
            return []


        # sorting numbers to get the smallest element, first check to know if k exist.
        nums = sorted(nums)
        n = len(nums)

        for i in range(1, n):
            # for each num after nums[0], check if this produces the perfect difference for
            # k to exist.
            diff = nums[i] - nums[0]

            # for k to exist diff should be even as k is middle of this difference.
            if(diff != 0 and diff % 2 == 0):
                res = k_exist(diff)
                if(res):
                    return res
