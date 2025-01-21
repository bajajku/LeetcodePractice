class Solution(object):
    def gridGame(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        '''
        1st robot greedily return path with maximum points
            -> this fails as robo1(red) dont want to maximize his points but minimize rob2's points,
                kinda evil I know.

        -> we set this path as 0

        2nd robot will take the path with most points greedily

        T.C = O(2n + n + 2n) == O((5n)),
        '''

        '''
        greedy fails
        '''
        '''
        Actual situation, as we cannot move top, left the options for rob 2 to move are quite limited
        he can only move down once, and that's it

        So robo 2 will only move the whole bottom row, or the whole top row
        now the question arises why?

        the answer is we know robo1 will always take a path that minimises robo2's result, so we dont actually  
        need to simulate robo1.
        We just assume it took it's best descision, we just have to simulate robo2 and determine it's best descion.

        Now, after robo1 does it's deed, what can robo 2 realistically do to maximise it's sum
        -> let see our rows == 2, and cols == 5

        let simulate robo1
        
        000xx
        xx000

        It turned in the middle, so we can see ach time it's either top or bottom

        let's do another

        00xxx
        x0000

        still the same, top row or bottom, just number of x changes each time.

        so we need minimum of these combination, as robo1 will always try to screw us.

        '''
        topRow = sum(grid[0])
        
        bottomRow = 0

        res = float("inf")

        for c in range(len(grid[0])):

            topRow -= grid[0][c]

            res = min(res, max(topRow, bottomRow))

            bottomRow += grid[1][c]
        
        return res





