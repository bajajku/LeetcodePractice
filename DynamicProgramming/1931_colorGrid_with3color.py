class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:

        MOD = 10 ** 9 + 7
        '''
            0 = no color
            1 = red
            2 = green
            3 = blue
        '''
        dp = [[-1] * 1024 for _ in range(1002)]
        
        def function(r, c, curr, prev):

            if c == n:
                return 1
            
            if r == m:
                return function(0, c + 1, 0, curr)
            
            if r == 0 and dp[c][prev] != -1:
                return dp[c][prev]

            up_color = 0 # 0 means no color
            if r > 0:
                up_color = curr & 3 # take the last 2 bits
            
            # right shift prev state to get adjacent left_color, and & by 3 to get last two bits.
            left_color = prev >> ((m - r - 1) * 2) & 3

            result = 0

            for color in range(1, 4):
                if color != up_color and color != left_color:
                    # left shift by two to get 00 bits for next stage, and fill that 
                    # 00 by relevant color (red[01], green[10], blue[11])
                    new_state = (curr << 2) | color

                    result += function(r + 1, c, new_state, prev) % MOD
            
            dp[c][prev] = result % MOD
            return result % MOD
        
        return function(0, 0, 0, 0)
