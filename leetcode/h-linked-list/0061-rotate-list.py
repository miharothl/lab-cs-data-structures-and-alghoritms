# https://leetcode.com/problems/rotate-list/
from typing import Optional

from _toolbox.LinkedList import ListNode
from _toolbox.LinkedListFactory import LinkedListFactory


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k==0:
            return head

        length = 1

        tail = head
        while head.next:
            head = head.next
            length += 1

        head.next = tail

        steps_to_new_tail = length - k

        for _ in range(steps_to_new_tail - 1):
            tail = tail.next

        new_head = tail.next
        tail.next = None

        return new_head

solution = Solution()

list = LinkedListFactory.array_to_linked_list([1, 2, 3, 4, 5])
k = 2
result = solution.rotateRight(list, k)
print("pass") if LinkedListFactory.linked_list_to_array(result) == [4, 5, 1, 2, 3] else print("fail")
