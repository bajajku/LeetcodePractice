class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        
        sorted_nums = sorted(nums)

        hm = {}

        queueMap = {}
        x = []
        init = sorted_nums[0]
        groupNum = 0

        queue = deque()

        for i in sorted_nums:


            if(abs(i - init) <= limit):
                hm[i] = groupNum
                queue.append(i)
                
            else:
                queueMap[groupNum] = queue
                groupNum += 1
                hm[i] = groupNum
                queue = deque([i])
            init = i
        
        queueMap[groupNum] = queue

        for i in range(len(nums)):
            n = nums[i]

            group_of_n = hm[n]

            nums[i] = queueMap[group_of_n].popleft()
        
        return(nums)
        
        

