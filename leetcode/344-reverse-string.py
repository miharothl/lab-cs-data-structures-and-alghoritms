class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        pl = 0
        ph = len(s) - 1

        while pl < ph:
            s[pl], s[ph] = s[ph], s[pl]

            pl += 1
            ph -= 1

        return s


solution = Solution()
print("pass") if solution.reverseString(["H", "a", "n", "n", "a", "h"]) == ["h", "a", "n", "n", "a", "H"] else print("fail")
print("pass") if solution.reverseString(["H"]) == ["H"] else print("fail")
print("pass") if solution.reverseString([]) == [] else print("fail")