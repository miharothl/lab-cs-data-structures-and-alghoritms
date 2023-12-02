# https://leetcode.com/problems/keys-and-rooms/
from typing import List


class Solution:

    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        seen = [False] * len(rooms)

        stack = []
        stack.append(0)

        while stack:
            node = stack.pop()

            if not seen[node]:
                seen[node] = True
                keys = rooms[node]

                for key in keys:
                    stack.append(key)
        return all(seen)


solution = Solution()

rooms = [[1], [2], [3], []]
print("Pass") if solution.canVisitAllRooms(rooms) == True else print("Fail")

rooms = [[1, 3], [3, 0, 1], [2], [0]]
print("Pass") if solution.canVisitAllRooms(rooms) == False else print("Fail")

"""
Problem: keys in rooms
Type: graph

Thinking:
* stack
* seen array with [False] * len(rooms)
* add first room to stack
* while stack pop node, if not visited add keys to stack

Complexity:
* Time: O(N+E) where N is number of nodes, and E number of edges
* Memory:O(N) to store stack and seen
"""

