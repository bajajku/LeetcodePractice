class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        # output is always in increasing order.
        # output can decrease too

        color_dict = {}
        hm = {}

        res = []
        count = 0

        for i, j in queries:
            if j not in hm or hm[j] == 0:
                hm[j] = 1
                count += 1
            else:
                hm[j] += 1

            if i in color_dict:
                
                hm[color_dict[i]] -= 1
                if hm[color_dict[i]] == 0:
                    count -= 1

            color_dict[i] = j

            if count == 0:
                res.append(1)
            else:
                res.append(count)

        return res
