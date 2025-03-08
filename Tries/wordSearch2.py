class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

    def addWord(self, word):
        cur = self
        for w in word:
            if(w not in cur.children):
                cur.children[w] = TrieNode()
            cur = cur.children[w]

        cur.endOfWord = True


class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        root = TrieNode()

        for word in words:
            root.addWord(word)
        
        rows, cols = len(board), len(board[0])
        res = set()
        visited = set()


        def dfs(r, c, curNode, word):

            if r < 0 or c < 0 or r == rows or c == cols or (r, c) in visited or board[r][c] not in curNode.children:
                return 


            visited.add((r, c))

            curNode = curNode.children[board[r][c]]

            word += board[r][c]

            if(curNode.endOfWord):
                res.add(word)

            dfs(r + 1, c, curNode, word)
            dfs(r - 1, c, curNode, word)
            dfs(r, c + 1, curNode, word)
            dfs(r, c - 1, curNode, word)

            visited.remove((r, c))

        
        for r in range(rows):
            for c in range(cols):

                dfs(r, c, root, "")

        
        return list(res)
            
            

