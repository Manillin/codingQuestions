class TrieNode:
    def __init__(self):
        self.children = {}
        self.EOW = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()


    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.EOW = True 

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False 
            cur = cur.children[c]
        return True if cur.EOW else False         

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False 
            cur = cur.children[c]
        return True 






        
        