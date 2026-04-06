/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public void reorderList(ListNode head) {
        ListNode slow = head;
        ListNode fast = head.next;
        while(fast != null && fast.next != null){
            slow = slow.next;
            fast = fast.next.next;
        }
        ListNode mid = slow.next;
        slow.next = null;
        ListNode prev = null;
        while(mid != null){
            ListNode temp = mid.next;
            mid.next = prev;
            prev = mid;
            mid = temp;
        }
        ListNode l2 = prev;
        while(l2 != null){
            ListNode t1 = head.next;
            ListNode t2 = l2.next;
            head.next = l2;
            l2.next = t1;
            head = t1;
            l2 = t2;
        }
    }
}
