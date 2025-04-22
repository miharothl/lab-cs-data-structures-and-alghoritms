# https://leetcode.com/problems/is-subsequence/

# class Solution:
#     def isSubsequence(self, s1: str, s2: str) -> bool:
#         n, m = len(s1), len(s2)
#         # edge case
#         if n > m:
#             return False
#         i, j = 0, 0
#         while (i < n and j < m):
#             if (s1[i] == s2[j]):
#                 i += 1
#             j += 1
#         return i == n

class Solution:

    def isSubsequence(self, s: str, t: str) -> bool:

        i, j = 0, 0

        while i < len(s) and j< len(t):

            if s[i] == t[j]:
                i += 1

            j += 1

        return i == len(s)





        # p0 = 0
        # p1 = 0
        #
        # debug = False
        #
        # found_subsequence = True
        #
        # for c in s:
        #     print(c) if debug else None
        #
        #     if not found_subsequence:
        #         return found_subsequence
        #
        #     while p1 < len(t):
        #         if t[p1] == c:
        #             print('found: {0}'.format(t[p1])) if debug else None
        #
        #             p1 += 1
        #             p0 = p1
        #             break
        #         else:
        #             print(t[p1]) if debug else None
        #             p1 += 1
        #     else:
        #         print('found not') if debug else None
        #         found_subsequence = False
        #
        # return found_subsequence


solution = Solution()

s = "abc"
t = "ahbgdc"
print("Pass") if solution.isSubsequence(s, t) is True else print("Fail")

s = "axc"
t = "ahbgdc"
print("Pass") if solution.isSubsequence(s, t) is False else print("Fail")



"""
Idea:
* use one pointer to track i, and another to track j
* if chars match move i forward
* allways move j forward
* if i reaches the end of s, all chars were matched in order --> its a subsequence

Time:
O(n)

Space:
O(1)
"""