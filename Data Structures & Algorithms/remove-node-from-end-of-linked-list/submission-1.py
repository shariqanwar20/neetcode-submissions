# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # find length of the list
        size = 0
        curr = head
        while curr:
            size += 1
            curr = curr.next
        

        # remove length - n (0-indexed)
        remove_ind = (size - n) + 1
        dummy = ListNode(None)
        dummy.next = head

        k = 0

        # # Edge case
        # if k == remove_ind: return None
        
        
        curr = dummy
        while curr:
            if (k + 1 == remove_ind):
                # remove 1 -> 2 -> 3 -> 4
                curr.next = curr.next.next
            curr = curr.next
            k += 1
        return dummy.next
