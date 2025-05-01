class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:


        n, m = len(tasks), len(workers)

        tasks.sort()
        workers.sort()

        def check(mid):
            boosted = deque() # to keep track of workers that gets boosted
            w = m - 1
            p = pills # copy of pills

            # loop through tasks in reversed order, i.e biggest tasks first (as tasks are sorted)
            # why [:mid], cause we want to do find can we do (mid = some x tasks)
            for t in reversed(tasks[:mid]):
                
                # if a boosted worker can complete the task then.
                if boosted and boosted[0] >= t:
                    boosted.popleft()
                
                # if worker without boost can do the task
                elif w >= 0 and workers[w] >= t:
                    w -= 1
                
                else:
                    # boost the workers that can complete the tasks, if they have more strength
                    while w >= 0 and workers[w] + strength >= t:
                        boosted.append(workers[w])
                        w -= 1
                    # if even boosted workers cannot complete the tasks, or pills are finished,
                    # then we can not do mid number of tasks, so return False
                    if not boosted or p == 0:
                        return False
                    
                    # to complete the current task after boosting
                    boosted.pop()
                    p -= 1
            
            # if we havent returned false yet, it means we can surely do mid num of tasks
            return True

        # basic binary search  
        l, r = 1, min(m, n)
        res = 0

        while l <= r:

            mid = (l + r) // 2

            if(check(mid)):
                res = mid
                l = mid + 1
            else:
                r = mid - 1
        
        return res 
