# https://leetcode.com/problems/odd-even-linked-list

from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None:
            return None

        odd_head = head
        odd = head
        even_head = head.next
        even = head.next

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = even_head

        return odd_head

    def to_array(self, head: Optional[ListNode]) -> List[int]:
        current = head

        res = []

        while current:
            res.append(current.val)

            current = current.next

        return res


solution = Solution()

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print("Pass") if solution.to_array(solution.oddEvenList(head)) == [1, 3, 5, 2, 4] else print("Fail")

head = ListNode(2, ListNode(1, ListNode(3, ListNode(5, ListNode(6, ListNode(4, ListNode(7)))))))
print("Pass") if solution.to_array(solution.oddEvenList(head)) == [2, 3, 6, 7, 1, 5, 4] else print("Fail")

head = None
print("Pass") if solution.to_array(solution.oddEvenList(head)) == [] else print("Fail")

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
print("Pass") if solution.to_array(solution.oddEvenList(head)) == [1, 3, 2, 4] else print("Fail")

"""
Problem: odd even linked list
Type: stack

Thinking:
* use to head pointers one even and one for odd elements
* use to tail pointers one even and one for odd elements
* tail pointers are also used as iterators
* attach even to odd list (even_head)
* return head of even list (odd_head)
* 

Complexity:
* Time: iterate through linked list with N elements O(N)
* Memory: in-place O(1)
"""
