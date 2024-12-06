def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums) -1

        while l <= r:

            mid = (l + r) // 2

            if nums[mid] == target:
                return mid

            # check if left half is sorted
            if(nums[l] <= nums[mid]):
                # check if target exist in left half
                if(nums[l] <= target and target < nums[mid]):
                    r = mid - 1
                else:
                    # switch to right half
                    l = mid + 1
            
            else: # if left half is not sprted right will ALWAYS be
                if(nums[mid] < target <= nums[r]):
                    # same logic as above
                    l = mid + 1
                else:
                    r = mid - 1

        return -1