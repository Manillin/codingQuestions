# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head 
        i = 0
        curr = head
        while i < n:
            fast = fast.next 
            i+=1
        if not fast:
            return head.next
        while fast.next:
            curr = curr.next 
            fast = fast.next 
        curr.next = curr.next.next 

        return head