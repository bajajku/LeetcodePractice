class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        # i can think of something like first occurence last occurence.

        a = set(s)
        hm = {i: [] for i in a}
        for i in range(len(s)):
            hm[s[i]].append(i)
        
        intervals = []

        for k, v in hm.items():
            intervals.append([v[0], v[-1]])
        
        
        intervals.sort(key=lambda pair: pair[0])
        output = [intervals[0]]

        for start, end in intervals:
            lastEnd = output[-1][1]

            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])
        
        res = []
        for l, r in output:
            res.append(r-l + 1)
        
        return res
        
