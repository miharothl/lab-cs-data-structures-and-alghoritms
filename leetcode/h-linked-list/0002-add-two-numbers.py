# https://leetcode.com/problems/add-two-numbers/
from _toolbox.LinkedListFactory import LinkedListFactory


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        carry = 0
        current = dummy

        while l1 or l2 or carry:

            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry

            carry = total // 10

            current.next = ListNode(total % 10)
            current = current.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next

solution = Solution()
list1 = LinkedListFactory.array_to_linked_list([2,4,3])
list2 = LinkedListFactory.array_to_linked_list([5,6,4])

result = solution.addTwoNumbers(list1, list2)
print("pass") if LinkedListFactory.linked_list_to_array(result) == [7,0,8] else print("fail")


"""
Idea:
* use Dummy node
* use carry 
* use // to 13 // 10 = 1  --- floor division 
* use %  to 13 % 10 = 3   --- modulo
* loop through the nodes using while l1, l2, carry:

Time:
O(max(n, m)) where n and m are lengths of lists

Space:
O(max(n, m)) where n and m are lengths of lists
"""