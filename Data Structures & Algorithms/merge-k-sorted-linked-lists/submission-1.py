# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: return None

        head = ListNode(-1)

        curr = head
        for i in range(1, len(lists)):
            lists[i] = self.merge_two_lists(lists[i-1], lists[i])

        return lists[-1]


    def merge_two_lists(self, l1, l2):
        head = ListNode(-1)

        curr = head
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next

            curr = curr.next

        if l1:
            curr.next = l1
        
        if l2:
            curr.next = l2

        return head.next
