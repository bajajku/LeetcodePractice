class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        visited = set()
        def function(r, c, string):
            
            if(len(string) == len(word)):
                if(string == word):
                    return True
            if(r == len(board) or c == len(board[0]) or r < 0 or c < 0 or (r,c) in visited):
                return False
    
            string = string + board[r][c]
            visited.add((r,c))
            left = function(r, c-1, string)
            right = function(r, c+1, string)
            top = function(r - 1, c, string)
            bot = function(r +1, c, string)

            string = string[:-1]
            visited.remove((r,c))

            return left or right or top or bot
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if(function(r, c, "")):
                    return True
        
        return False


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        Rows, Cols = len(board), len(board[0])

        visited = set()
        def backtrack(r, c, i):
            if(i == len(word)):
                return True

            if(r < 0 or c < 0 or r >= Rows or c >= Cols or board[r][c] != word[i] or (r,c) in visited):
                return False

            visited.add((r,c))

            # checking for all possible situations
            result = backtrack(r + 1, c, i + 1) or backtrack(r - 1, c, i+1) or backtrack(r, c+1, i+1) or backtrack(r, c-1, i+1) 

            visited.remove((r,c))
            return result

        for r in range(Rows):
            for c in range(Cols):
                if backtrack(r, c, 0):
                    return True
            
        return False
