# https://leetcode.com/problems/length-of-last-word/

class Solution:
    def lengthOfLastWord_python(self, s: str) -> int:
        words = s.strip().split()
        return len(words[-1])

    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1

        while i >= 0 and s[i] == ' ':
            i -= 1

        length = 0

        while i >= 0 and s[i] != ' ':
            i -= 1
            length += 1

        return length

solution = Solution()

s = "   fly me   to   the moon  "
print("pass") if solution.lengthOfLastWord_python(s) == 4 else print("fail")

s = "   fly me   to   the moon  "
print("pass") if solution.lengthOfLastWord(s) == 4 else print("fail")

s = "luffy is still joyboy"
print("pass") if solution.lengthOfLastWord(s) == 6 else print("fail")


"""
Idea:
* traverse from back
* skip spaces
* count length of the first word

Time:
O(n) - one pass through the string

Space:
O(1) -- in-place

"""