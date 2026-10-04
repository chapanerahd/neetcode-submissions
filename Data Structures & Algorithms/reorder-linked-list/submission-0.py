# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        def midpoint(node):
            slow = fast = node
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            
            return slow
        
        def reverse(node):
            prev = None
            while node:
                nxt_node = node.next
                node.next = prev
                prev = node
                node = nxt_node
            return prev
        
        def merge(l1, l2):
            if not l1 or not l2:
                return l1 or l2

            dummy = ListNode(-1)
            curr = dummy
            while l1 and l2:
                nxt_l1 = l1.next
                nxt_l2 = l2.next

                curr.next = l1
                curr = curr.next
                curr.next = l2
                curr = curr.next

                l1 = nxt_l1
                l2 = nxt_l2

            if l1 or l2:
                curr.next = l1 or l2

            return dummy.next


        middle = midpoint(head)        
        next_ll = middle.next
        middle.next = None
        reverse_ll = reverse(next_ll)
        merge(head, reverse_ll)

