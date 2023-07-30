# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow

    # def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     size = self.getSize(head)
    #
    #     mid = head
    #     node = head
    #
    #     count = 0
    #
    #     while node:
    #         node = node.next
    #         count += 1
    #
    #         if count % 2 == 0:
    #             mid = mid.next
    #
    #     return mid

head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

solution = Solution()
print("pass") if solution.middleNode(head1).val == 3 else print("fail")

head2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
print("pass") if solution.middleNode(head2).val == 4 else print("fail")
