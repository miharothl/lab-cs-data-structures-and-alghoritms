class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        dict = {}
        p0 = p1 = 0
        counter = 0

        while p0 < len(s) and p1 < len(s):

            char = s[p1]

            if char in dict:
                p0 = max(p0, dict[char] + 1)

            dict[char] = p1

            counter = max(counter, p1 - p0 + 1)

            p1 += 1

        return counter


solution = Solution()
print("pass") if solution.lengthOfLongestSubstring("abcabcbb") == 3 else print("fail")
print("pass") if solution.lengthOfLongestSubstring("bbbb") == 1 else print("fail")
print("pass") if solution.lengthOfLongestSubstring("pwwkew") == 3 else print("fail")