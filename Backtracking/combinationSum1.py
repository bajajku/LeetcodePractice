class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        def function(index, target, combo):

            if(index == 0):
                if(target % candidates[index] == 0):
                    for j in range(target // candidates[index]):
                        combo.append(candidates[index])
                    res.append(combo[::])
                    return
                else:
                    return
            
            nPick = function(index -1, target, combo[::])

            if(target >= candidates[index]):
                c = combo[::]
                c.append(candidates[index])
                pick = function(index, target - candidates[index], c)

            return
        
        function(len(candidates) -1, target, [])
        
        return(res)


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        def function(index, target, combo):

            if(target == 0):
                res.append(combo[:])
                return
            
            if target < 0 or index == len(candidates):
                return
            
            
            combo.append(candidates[index])
            function(index, target - candidates[index], combo)
            combo.pop()
            function(index+1, target, combo)

        
        function(0, target, [])
        
        return(res)
