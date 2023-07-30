# https://leetcode.com/problems/reverse-linked-list/
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        current = head
        prev = None
        next = None
        while current != None:
            # save the next node
            next = current.next

            # reverse the link to previous node
            current.next = prev

            # move prev, current nodes to next node
            prev = current
            current = next

        return prev


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

solution = Solution()
reversed = solution.reverseList(head)

print("pass") if (reversed.val == 5 and
                  reversed.next.val == 4 and
                  reversed.next.next.next.next.val == 1 and
                  reversed.next.next.next.next.next == None) else print("fail")

"""
Problem: reverse linked list
Type: linked list

Thinking:
* create current, next, prev pointers
* traverse linked list
* set next to current.next
* reverse pointers by setting current.next to prev
* move nodes forward

Complexity:
* Time: O(N)
* Memory:O(1)
"""

