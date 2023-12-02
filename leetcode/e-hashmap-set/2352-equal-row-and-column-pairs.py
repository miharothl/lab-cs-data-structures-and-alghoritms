# https://leetcode.com/problems/equal-row-and-column-pairs
import collections
from typing import List

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:

        row_counter = {}

        for row in grid:
            # key = "-".join(str(r) for r in row)
            key = tuple(row)
            # print(key)

            if key in row_counter.keys():
                row_counter[key] += 1
            else:
                row_counter[key] = 1

        # print(row_counter)

        pair_counter = 0
        for i in range(len(grid)):
            # key = "-".join(str(grid[j][i]) for j in range(len(grid)))
            col = [grid[j][i] for j in range(len(grid))]
            key = tuple(col)
            # print(key)

            if key in row_counter.keys():
                pair_counter += row_counter[key]

        return pair_counter

solution = Solution()

grid = [[13, 13], [13, 13]]
print("Pass") if solution.equalPairs(grid) == 4 else print("Fail")

grid = [[3, 2, 1], [1, 7, 6], [2, 7, 7]]
print("Pass") if solution.equalPairs(grid) == 1 else print("Fail")

grid = [[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]
print("Pass") if solution.equalPairs(grid) == 3 else print("Fail")


"""
Problem: equal row and column pairs
Type: hash table

Thinking:
* use tuple for a key
* traverse the rows and count the frequency in hash table
* traverse thw cols
  * if key in hashtable
  * add frequency for that key to the pair_counter

Complexity:
let N x N is the size of the grid
* Time: 1. traverse the row, col
          O(N)
        2. to calculate the column key two nested for loops
          O(N*N)
* Space:
        1. to store the hash table
           worst case scenario O(N*N), to store N rows with N columns
"""
