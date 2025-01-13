class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()  # Sort the candidates to handle duplicates

        def function(index, target, combo):
            # Base case: If the target is 0, add the combination to results
            if(target == 0):
                res.append(combo[:])
                return
            
            for i in range(index, len(candidates)):

                if(i > index and candidates[i] == candidates[i-1]):
                    continue
                
                if candidates[i] > target:
                    break
                
                combo.append(candidates[i])
                function(i + 1, target - candidates[i], combo)
                combo.pop()
        
        function(0, target, [])
        return res
