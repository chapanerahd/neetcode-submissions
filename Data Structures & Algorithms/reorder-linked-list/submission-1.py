# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def get_mid(node):
            slow = fast = node
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            
            return slow
        
        def reverse(node):
            prev = None
            curr = node
            while curr:
                nxt_node = curr.next
                curr.next = prev
                prev = curr
                curr = nxt_node
            return prev
        
        def merge(l1, l2):
            dummy = ListNode(-1)
            curr = dummy
            while l1 and l2:
                curr.next = l1
                l1 = l1.next
                curr = curr.next
                curr.next = l2
                l2 = l2.next
                curr = curr.next
            
            curr.next = l1 or l2
            
            return dummy.next

        mid = get_mid(head)
        nxt_head = mid.next
        mid.next = None
        mid_reverse = reverse(nxt_head)
        merge(head, mid_reverse)
