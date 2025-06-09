class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        
        '''
        Main intuition is Trie trees:

        So there is two ways we can move in lexographical order:
            -> Horizontally (Right the Trie):
                Ex: 1xx -> 2xx
            -> Vertically (Down the Trie):
                Ex: 1xx -> 1xx0
        
        So now question arises when to move where:
            -> So to move horizontally we need to know that remaining k >= (numbers between 1xx and 2xx for example)
            -> And to move vertically if (numbers between 1xx and 2xx for example) > k we move to next vertical step
                as, we might need to search more thoroughly there.
        
        TC: Time complexity: O(log(n)^2)
        
        
        '''
        def count_steps(prefix1, prefix2):
            steps = 0
            while prefix1 <= n:
                steps += min(prefix2, n + 1) - prefix1 
                prefix1 *= 10
                prefix2 *= 10
            
            return steps
        
        cur = 1

        k -= 1

        while k > 0:
            
            steps = count_steps(cur, cur + 1)

            if steps <= k:
                cur += 1
                k -= steps
            
            else:
                cur *= 10
                k -= 1
        
        return cur

