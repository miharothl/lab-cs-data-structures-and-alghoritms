# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        length = self.countElements(head)
        middle = int(length / 2)

        count = 0

        current = head
        prev = None
        next = None
        while count <= middle:

            next = current.next

            if count == middle:
                if prev is not None:
                    prev.next = next
                else:
                    return None

            count += 1

            prev = current
            current = next

        return head

    def countElements(self, head: Optional[ListNode]) -> int:
        count = 0

        current = head
        while current:
            count += 1
            current = current.next

        return count



solution = Solution()

head = ListNode(1, ListNode(3, ListNode(4, ListNode(7, ListNode(1, ListNode(2, ListNode(6)))))))
deleted = solution.deleteMiddle(head)
print("pass") if (deleted.next.next.next.val == 1 and
                  deleted.next.next.next.next.val == 2 and
                  deleted.next.next.next.next.next.val and
                  deleted.next.next.next.next.next.next == None) else print("fail")

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
deleted = solution.deleteMiddle(head)
print("pass") if (deleted.next.val == 2 and
                  deleted.next.next.val == 4 and
                  deleted.next.next.next == None) else print("fail")

head = ListNode(1, ListNode(2))
deleted = solution.deleteMiddle(head)
print("pass") if (deleted.val == 1 and
                  deleted.next == None) else print("fail")

head = ListNode(1)
deleted = solution.deleteMiddle(head)
print("pass") if deleted == None else print("fail")

"""
Problem: delete the middle node of a linked list
Type: linked list

Thinking:
* traverse linked list and count elements
* calculate middle
* create current, next, prev pointers
* traverse linked list until count <= middle
* set next to current.next
* if count is middle remove element
* increase count
* move nodes forward

Complexity:
* Time: O(N)
* Memory:O(1)
"""

