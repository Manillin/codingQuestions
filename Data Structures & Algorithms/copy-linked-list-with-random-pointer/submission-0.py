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
        oldnew = {None:None}
        curr = head
        while curr:
            if curr not in oldnew:
                new_node = Node(curr.val,None,None)
                oldnew[curr] = new_node 
            curr = curr.next
        curr = head
        while curr:
            new_node = oldnew[curr]
            new_node.next = oldnew[curr.next]
            new_node.random = oldnew[curr.random]
            curr = curr.next 
        return oldnew[head]
