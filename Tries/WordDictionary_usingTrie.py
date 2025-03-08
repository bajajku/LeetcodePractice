class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False  # Marks the end of a word

class WordDictionary(object):

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        cur = self.root
        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()
            cur = cur.children[w]
        cur.isEnd = True  # Mark end of the word
    
    def dfs(self, index, node, word):
        """
        Depth-first search to check for a match.
        """
        if index == len(word):
            return node.isEnd  # Ensure we reached an actual word end

        char = word[index]
        if char != ".":  # Regular character search
            if char not in node.children:
                return False
            return self.dfs(index + 1, node.children[char], word)
        
        # If character is '.', try all possible children
        for child in node.children.values():
            if self.dfs(index + 1, child, word):
                return True

        return False

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return self.dfs(0, self.root, word)


# Example Usage:
# obj = WordDictionary()
# obj.addWord("bad")
# obj.addWord("dad")
# obj.addWord("mad")
# print(obj.search("pad"))  # False
# print(obj.search("bad"))  # True
# print(obj.search(".ad"))  # True
# print(obj.search("b.."))  # True
