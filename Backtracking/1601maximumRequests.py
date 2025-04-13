class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        
        '''
        Given: 
            -> n buildings: [0...n-1]
            building (n):
                -> num employees (n)
            
            requests: [from_i, to_i]
                represents employee request transfer from building from_i ---> to to_i
                Ex:
                [0, 1]
                Employee wants to transfer from_0 --> to_1

            All buildings are full, so a list of request uis achievable if for each building,
            the net change in employee transfer is 0
            i.e (num emp leaving == num emp moving)

            Example:
            if n = 3, i.e three buildings

            0 -> 2 emp leaving, then 2 moving
            1 -> 1 emp leaving, then 1 moving
            2 -> 2 emp leaving, then 2 moving
        
        Return:
            max number of achievable requests:

        
        Dry Run example:
    Example: 1
        n = 5, requests = [[0,1],[1,0],[0,1],[1,2],[2,0],[3,4]]

        x = 0 -> 1
        y = 1 -> 0
        z = 0 -> 1
        a = 1 -> 2
        b = 2 -> 0
        c = 3 -> 4

        hm_leav = {0: 2, 1: 2, 2: 1, 3: 1, 4: 0}
        hm_mov = {0: 2, 1: 2, 2: 1, 4: 1, 3: 0 }


    Example: 2
        n = 3, requests = [[0,0],[1,2],[2,1]]

        x = 0 -> 0
        y = 1 -> 2
        z = 2 -> 1

        hm_leav = {0: 1, 1: 1, 2: 1}
        hm_mov = {0: 1, 1: 1, 2: 1}

    Example 3:
        n = 4, requests = [[0,3],[3,1],[1,2],[2,0]]

        x = 0 -> 3
        y = 3 -> 1
        z = 1 -> 2
        a = 2 -> 0

        hm_leav = {0: 1, 1: 1, 2: 1, 3: 1}
        hm_mov = {0: 1, 1: 1, 2: 1, 3: 1}

    ** From these examples it looks like create hashMaps and compare frequencies if frequenciens 
       of same building match then add in res **

    
    Example: 4
    n = 5, requests = [[0,3],[3,1],[1,2],[2,0],[3,2],[4,3]]

        x = 0 -> 3
        y = 3 -> 1
        z = 1 -> 2
        a = 2 -> 0
        b = 3 -> 2
        c = 4 -> 3

        hm_leav = {0: 1, 1: 1, 2: 1, 3: 2, 4: 1}
        hm_mov = {0: 1, 1: 1, 2: 2, 3: 2, 4: 0}
        
        '''
        
        arr = [0] * n


        def function(i, reqs, arr):

            if i == len(requests):
                if arr == ([0] * n):
                    return reqs
                return float("-inf")
            
            # pick case
            from_i = requests[i][0]
            to_i = requests[i][1]

            # pick case
            arr[from_i] -= 1
            arr[to_i] += 1
            pickR = function(i + 1, reqs + 1, arr)
            
            # recursive cleanup
            arr[from_i] += 1
            arr[to_i] -= 1

            nPickR = function(i + 1, reqs, arr)

            return max(pickR, nPickR)

        return function(0, 0, arr)


        '''
            Feedback for me: 
                W's:
                1) Good approach of breaking down question in comments
                2) Nice run on examples
                3) Good find that hashmap won't work which looked it works from examples
                4) Solved in one try after hints.

                L's:
                1) Should have read constraints, and think of backtrack myself, as approach is not too difficult.

        
        '''


    
