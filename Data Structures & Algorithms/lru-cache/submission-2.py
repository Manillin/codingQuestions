class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value 
        self.next = None 
        self.prev = None 

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {} # key , node 
        self.cap = capacity
        self.right = Node(0,0)
        self.left = Node(0,0)
        self.right.prev = self.left 
        self.left.next = self.right 

    def remove(self, node):
        prev = node.prev 
        nxt = node.next 
        prev.next = nxt 
        nxt.prev = prev 

    def insert(self,node):
        nxt = self.right 
        prev = nxt.prev 
        prev.next = node 
        node.next = nxt 
        nxt.prev = node 
        node.prev = prev 
    
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1 

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)
        
        if len(self.cache) > self.cap:
            lru = self.left.next.key
            self.remove(self.cache[lru])
            del self.cache[lru]
