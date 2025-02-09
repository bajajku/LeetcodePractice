class Solution:
    def countBadPairs(self, nums: List[int]) -> int:

        '''so what are bad pairs, something that's not good
        
        Einstien: "Invert always invert" --> If you are unable to figure something or want to have a deep thinking about something opposite that situations.

        so to solve what are bad pairs we can figure out what are good pairs instead

        good pairs are something whose:

        nums[i] - i = nums[j] - j, mean have same weight which we can derive from the equation.

        Now what are total pairs:

        total pairs using this formula: n(n-1) // 2 

        why this formula, it is nCr, r == 2 as we want pairs

        similary how to calculate good pairs:

        we can store count for each weight(nums[i] - i) in a hashMap

        and for each key of hashMap, where val > 1, i.e we can form a pair we will calculate 
        the good pairs.
        
        '''

        freq = {}
        good_pairs = 0

        for i, num in enumerate(nums):
            key = num - i
            good_pairs += freq.get(key, 0)
            freq[key] = freq.get(key, 0) + 1

        n = len(nums)
        return (n * (n - 1)) // 2 - good_pairs

      # second ways works faster.
        goodPair = {}

        for i, val in enumerate(nums):

            if((val - i) in goodPair):
                goodPair[val -i] += 1
            else:
                goodPair[val -i] = 1

        n = len(nums)
        total_pairs = (n * (n-1)) // 2

        gp = sum(((v-1) * v // 2) for v in goodPair.values())

        return total_pairs - gp
