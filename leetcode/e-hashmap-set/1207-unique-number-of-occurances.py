# https://leetcode.com/problems/unique-number-of-occurrences/
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        debug = False

        _map = {}
        _set = set([])

        for item in arr:
            print(item) if debug else None

            if item not in _map.keys():
                _map[item] = 1
            else:
                _map[item] += 1

        for key in _map.keys():
            _set.add(_map[key])

        print(_map) if debug else None
        print(_set) if debug else None

        if len(_set) == len(_map.keys()):
            return True
        else:
            return False


solution = Solution()

arr = [1, 2, 2, 1, 1, 3]
print("Pass") if solution.uniqueOccurrences(arr) is True else print("Fail")

arr = [1, 2]
print("Pass") if solution.uniqueOccurrences(arr) is False else print("Fail")

arr = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]
print("Pass") if solution.uniqueOccurrences(arr) is True else print("Fail")


"""
Problem: unique occurrences
Type: map, set

Thinking:
* find number of occurrences using hash table
* check unique number of occurrences using set

Complexity:
* Time: O(N)
* Memory:O(N)
"""