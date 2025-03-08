class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie(object):

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        cur = self.root

        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()
            cur = cur.children[w]

        cur.endOfWord = True
            
    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        cur = self.root
        for w in word:
            if w not in cur.children:
                return False
            cur = cur.children[w]
        
        return cur.endOfWord
        

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """

        cur = self.root

        for w in prefix:
            if w not in cur.children:
                return False
            cur = cur.children[w]
        
        return True

        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
