# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 0 1 2 3
        # 6 5 4 3

        # 2 4 6
        # 10 8

        # 2 4 None
        # 8 6 None

        # 2 4 6 None
        # 8 6 None

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
        prev = second_half.next = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        curr1 = head
        curr2 = prev

        while curr1 and curr2:
            temp1 = curr1.next
            temp2 = curr2.next
            curr1.next = curr2
            curr2.next = temp1
            curr1, curr2 = temp1, temp2

        if curr2:
            curr2.next = curr2



        
