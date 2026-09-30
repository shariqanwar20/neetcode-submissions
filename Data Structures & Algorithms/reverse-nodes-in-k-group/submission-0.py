# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 4. keep a start dummy node
        new_head = ListNode("dummy")
        new_head.next = head
        
        # 1. find size of list. gives an idea where to stop (length - length % k)
        list_size = self.size(head)
        end_ind = list_size - (list_size % k)

        # 2. reverse utility. reverse k node from start node given
        # 3. keep track of prev and next before/after k-node block respectively
        curr = head
        before, tail = new_head, curr
        for _ in range(0, end_ind - k, k):
            (k_node_head, start_of_next_k_group) = self.reverse(curr, k)
            before.next = k_node_head
            tail.next = curr = start_of_next_k_group
            before = tail
            tail = curr

        # final group
        (k_node_head, start_of_next_k_group) = self.reverse(curr, k)
        before.next = k_node_head

        # append remaining < k nodes
        
        if start_of_next_k_group:
            tail.next = start_of_next_k_group

        return new_head.next

    def size(self, node):
        count = 0
        curr = node
        while curr:
            count += 1
            curr = curr.next
        return count
    
    def reverse(self, node, k):
        curr, prev = node, None
        count = 0
        while curr:
            if count == k:
                break
            count += 1
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return (prev, curr)    