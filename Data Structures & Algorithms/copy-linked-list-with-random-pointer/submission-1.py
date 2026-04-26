"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldnew = defaultdict(lambda: Node(0))
        oldnew[None] = None 
        curr = head
        while curr:
            oldnew[curr].val = curr.val 
            oldnew[curr].next = oldnew[curr.next]
            oldnew[curr].random = oldnew[curr.random]
            curr = curr.next 
        return oldnew[head]
