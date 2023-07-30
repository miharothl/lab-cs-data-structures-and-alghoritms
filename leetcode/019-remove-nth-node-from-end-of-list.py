# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    def getSize(self, head: Optional[ListNode]):

        count = 0

        node = head
        while node:
            node = node.next
            count += 1

        return count

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = fast = head

        for i in range(n):
            fast = fast.next

        if not fast:
            return head.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return head

    # def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    #
    #     # traverse to get getSize
    #     # i_removeNode = size - n
    #     # traverse to remove
    #
    #     size = self.getSize(head)
    #     i_removeNode = size - n
    #     i_beforeNode = i_removeNode - 1
    #
    #     if i_beforeNode < 0:
    #         return head.next
    #
    #     node = head
    #
    #     for i in range(i_beforeNode):
    #         node = node.next
    #
    #     node.next = node.next.next
    #
    #     return head


head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

solution = Solution()
print("pass") if solution.removeNthFromEnd(head1, 2).next.next.next.val == 5 else print("fail")


head2 = ListNode(1)
print("pass") if solution.removeNthFromEnd(head2, 1) == None else print("fail")

head3 = ListNode(1, ListNode(2))
sol3 = solution.removeNthFromEnd(head3, 1)
print("pass") if (sol3.next == None and sol3.val == 1) else print("fail")

head4 = ListNode(1, ListNode(2))
sol4 = solution.removeNthFromEnd(head4, 2)
print("pass") if sol4.val == 2 else print("fail")
