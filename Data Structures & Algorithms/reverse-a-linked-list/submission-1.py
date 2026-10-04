# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def reverse(node, prev=None):
            if not node:
                return prev
            
            nxt_node = node.next
            node.next = prev
            return reverse(nxt_node, node)
        
        
        prev = None
        while head:
            nxt_node = head.next
            head.next = prev
            prev = head
            head = nxt_node
        return prev
