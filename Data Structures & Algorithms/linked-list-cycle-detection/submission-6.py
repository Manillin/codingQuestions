# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        fast = head.next 
        while fast and fast.next:
            if head == fast:
                return True 
            head = head.next 
            fast = fast.next.next
        return False