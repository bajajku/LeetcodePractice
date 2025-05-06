class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        
        MOD = 10 ** 9 + 7
        buyHeap = [] # this will store buy backlog in [in descending]
        sellHeap = [] # this will store sell backlog [in ascending]
        
        heapq.heapify(buyHeap)
        heapq.heapify(sellHeap)

        for price, amount, orderType in orders:
            
            # buy orders
            if orderType == 0:
                while sellHeap and sellHeap[0][0] <= price and amount > 0:
                    p, count = heapq.heappop(sellHeap)
                    if (count > amount):
                        heapq.heappush(sellHeap, (p, count - amount))
                    amount -= min(amount, count)
                if amount > 0:
                    heapq.heappush(buyHeap, (-price, amount))
            
            # sell orders
            elif orderType == 1:
                while buyHeap and -buyHeap[0][0] >= price and amount > 0:
                    p, count = heapq.heappop(buyHeap)
                    if (count > amount):
                        heapq.heappush(buyHeap, (p, count - amount))
                    amount -= min(amount, count)
                if amount > 0:
                    heapq.heappush(sellHeap, (price, amount))
        
        res = 0
        for k, val in sellHeap + buyHeap:
            res += val % MOD

        return res % MOD
