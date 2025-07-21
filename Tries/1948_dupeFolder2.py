class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        self.res = []
        class Trie:
            def __init__(self, val):
                self.val = val
                self.children = {}
                self.remove = False
                self.map = {}

            def insert(self, string):
                charSet = string
                cur = self
                for char in charSet:
                    if char in cur.children:
                        cur = cur.children[char]
                        continue
                    cur.children[char] = Trie(char)
                    cur = cur.children[char]
            
            def serialize_and_mark(self):
                
                cur = self

                def backtrack(node, par):

                    if node.children == {}:
                        return ""  # FIX 1: Return empty string for leaf nodes
                        
                    
                    res = ""
                    for child in sorted(node.children):  # sort to ensure deterministic order
                        res += "[" + child + backtrack(node.children[child], node) + "]"
                    
                    if res in cur.map:
                        cur.map[res].remove = True
                        node.remove = True  # FIX 2: Mark current node, not parent
                    else:
                        cur.map[res] = node
                    return res
                
                backtrack(cur, None)
                    
        def deserialize(node):

            def backtrack(node, cur):

                if node.remove == False:
                    if cur:  # FIX 3: Only add non-empty paths (skip root)
                        self.res.append(cur[:])
                

                for child in node.children.keys():
                    if node.children[child].remove:
                        continue
                    backtrack(node.children[child], cur + [child])
            
            backtrack(node, [])


        trie = Trie("/")
        for path in paths:
            trie.insert(path)
        
        trie.serialize_and_mark()

        deserialize(trie)
        return(self.res)
