# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

class Solution:
    def str_str_window(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)

        for i in range(n-m+1):

            if haystack[i:i+m] == needle:
                return i

        return -1




solution = Solution()

haystack = "sadbutsad"
needle = "sad"

print("pass") if solution.str_str_window(haystack, needle) == 0 else print("fail")
