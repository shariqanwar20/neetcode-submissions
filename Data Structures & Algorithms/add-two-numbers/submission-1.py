# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def getNumberFromList(head):
            curr = head
            power, res = 1, 0
            while curr:
                res = res + (curr.val * power)
                curr = curr.next
                power *= 10
            return res

        def getListFromNumber(value):
            if value == 0:
                return ListNode(value)
            curr = head = ListNode("dummy")
            while value != 0:
                curr.next = ListNode((value % 10))
                curr = curr.next
                value = value // 10
            return head.next
        
        return getListFromNumber(getNumberFromList(l1) + getNumberFromList(l2))