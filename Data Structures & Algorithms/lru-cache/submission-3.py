class Node:
    def __init__(self, key, value):
        self.key = key 
        self.val = value 
        self.prev = None 
        self.next = None 

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity 
        self.right, self.left = Node(0,0), Node(0,0)
        self.right.prev = self.left 
        self.left.next = self.right
    

    def insert(self, node):
        nxt = self.right 
        prev = self.right.prev 
        node.next = nxt 
        node.prev = prev 
        prev.next = node 
        nxt.prev = node 

    # prev = N = next 
    def remove(self, node):
        prev = node.prev 
        nxt = node.next 
        prev.next = nxt 
        nxt.prev = prev 

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1 

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next 
            self.remove(lru)
            del self.cache[lru.key]





