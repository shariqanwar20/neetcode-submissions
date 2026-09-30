# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def find_mid(head):
            parent = None
            slow, fast = head, head.next

            while fast and fast.next:
                parent = slow
                slow = slow.next
                fast = fast.next.next
            return slow
        
        second_half = find_mid(head)

        # reverse second half
        curr = second_half.next
        second_half.next = None
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        

        # merge the two lists
        
        # 2  4 3 None
        # | /|/
        # 8  6 None
        l1, l2 = head, prev
        while l1 and l2:
            temp1, temp2 = l1.next, l2.next
            l1.next = l2
            l2.next = temp1
            l1, l2 = temp1, temp2








