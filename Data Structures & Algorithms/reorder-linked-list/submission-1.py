# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head

        while curr.next:
            nxt = curr.next
            bLast, last = curr, nxt

            while last.next:
                bLast = bLast.next
                last = last.next

            curr.next = last
            if not last is nxt:
                last.next = nxt
                curr = nxt
                bLast.next = None
            else:
                break
            
            
        
        