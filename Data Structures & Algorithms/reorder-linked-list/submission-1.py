# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return None 
        fast = head.next
        curr = head 
        while fast and fast.next:
            curr = curr.next 
            fast = fast.next.next 
        l2 = curr.next
        prev = curr.next = None 
        while l2:
            temp = l2.next 
            l2.next = prev 
            prev = l2 
            l2 = temp 
        l2 = prev

        while head and l2:
            tmp1,tmp2 = head.next, l2.next 
            head.next = l2 
            l2.next = tmp1
            head = tmp1
            l2 = tmp2
        
