# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # got two linked list
        # 1. find middle point with slow-fast pointer 2. divide into two linked lists 3. merge two linked list

        # slow fast pointer (O(n) time and O(1) space)
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None
        # reverse second half linked list
        # 1 → 2 → 3 → None
        # None ← 1 ← 2 ← 3
        prev = None
        curr = second
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        # prev is now the head of the reversed second half
        first = head
        second = prev

        # 3. Interleave the two lists
        while second:
            first_next = first.next
            second_next = second.next

            first.next = second
            second.next = first_next

            first = first_next
            second = second_next


        