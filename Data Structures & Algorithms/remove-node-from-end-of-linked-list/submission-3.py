# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyNode = ListNode(0,head)
        curr = dummyNode 
        fast = head 

        while n > 0:
            fast = fast.next 
            n-=1
        while fast:
            fast= fast.next 
            curr = curr.next 
        curr.next = curr.next.next 
        return dummyNode.next 
