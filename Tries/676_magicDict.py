class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
    
    def insert(self, word):
        cur = self
        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()
            cur = cur.children[w]
        
        cur.endOfWord = True


    
    # def check(self, word):




class MagicDictionary:

    def __init__(self):
        self.structure = TrieNode()


    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.structure.insert(word)
    
    def dfs(self, off, node, cur, word):

        if(cur >= len(word)):
            if(node.endOfWord == True and off == False):
                return True
            return False

        if(off == False):
            if(word[cur] not in node.children):
                return False
            return self.dfs(False, node.children[word[cur]], cur + 1, word)
        else:
            for child in node.children:
                if child == word[cur]:
                    if self.dfs(True, node.children[child], cur + 1, word):
                        return True
                else:
                    if self.dfs(False, node.children[child], cur + 1, word):
                        return True
        return False

    def search(self, searchWord: str) -> bool:

        return self.dfs(True, self.structure, 0, searchWord)
        

        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
