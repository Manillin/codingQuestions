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
    public ListNode mergeKLists(ListNode[] lists) {
        // Handle empty input
        if (lists == null || lists.length == 0) {
            return null;
        }

        // Repeatedly merge pairs of lists until one list remains
        while (lists.length > 1) {
            int mergedSize = (lists.length + 1) / 2;
            ListNode[] mergedLists = new ListNode[mergedSize];

            int index = 0;

            // Merge lists in pairs: (0,1), (2,3), (4,5), ...
            for (int i = 0; i < lists.length; i += 2) {
                ListNode l1 = lists[i];
                ListNode l2 = (i + 1 < lists.length) ? lists[i + 1] : null;
                mergedLists[index++] = mergeTwoLists(l1, l2);
            }

            // Move to the next round
            lists = mergedLists;
        }

        // Final merged list
        return lists[0];
    }

    private ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        // Dummy node to simplify result list construction
        ListNode dummy = new ListNode(0);
        ListNode tail = dummy;

        // Merge while both lists still have nodes
        while (l1 != null && l2 != null) {
            if (l1.val <= l2.val) {
                tail.next = l1;
                l1 = l1.next;
            } else {
                tail.next = l2;
                l2 = l2.next;
            }
            tail = tail.next;
        }

        // Attach the remaining nodes from the non-empty list
        if (l1 != null) {
            tail.next = l1;
        } else {
            tail.next = l2;
        }

        return dummy.next;
    }
}