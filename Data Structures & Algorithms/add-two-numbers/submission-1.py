# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = curr = ListNode
        while l1 or l2 or carry > 0:

            op1 = l1.val if l1 else 0 
            op2 = l2.val if l2 else 0 
            node_val = op1+op2+carry
            if carry == 1:
                carry = 0
            if node_val >= 10:
                carry = 1
                node_val = node_val % 10 
            new_node = ListNode(node_val)
            curr.next = new_node
            if l1:
                l1 = l1.next 
            else:
                l1 = None 
            if l2:
                l2 = l2.next
            else:
                l2 = None 
            curr = curr.next 

        return dummy.next
            


