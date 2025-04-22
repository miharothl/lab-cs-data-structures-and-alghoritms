# https://leetcode.com/problems/isomorphic-strings/


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_to_t = {}
        t_to_s = {}

        for cs, ct in zip(s, t):
            if cs not in s_to_t:
                s_to_t[cs] = ct
            else:
                if s_to_t[cs] != ct:
                    return False

            if ct not in t_to_s:
                t_to_s[ct] = cs
            else:
                if t_to_s[ct] != cs:
                    return False

        return True




solution = Solution()

s = "add"
t = "foo"
print("pass") if solution.isIsomorphic(s, t) == True else print("fail")


s = "add"
t = "ffo"
print("pass") if solution.isIsomorphic(s, t) == False else print("fail")

"""
Idea:
* use two hash tables for mapping, s_to_t, t_to_s
* iterate through both arrays using zip
** add mapping s_to_t if not exist, otherwise check if the mapping is the same, if not return False
** add mapping t_to_s if not exist, otherwise check if the mapping is the same, it not return False

Time Complexity:
O(N) - one pass through array

Space Complexity:
O(N) - two hash maps

"""