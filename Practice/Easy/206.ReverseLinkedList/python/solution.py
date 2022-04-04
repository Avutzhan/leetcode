# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0.Problem, next=None):
#         self.val = val
#         self.next = next
# Iterative solution T: O(n) M: O(1)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev