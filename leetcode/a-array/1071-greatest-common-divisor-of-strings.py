class Solution:

    # great common string divisor
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        p1 = 0
        p2 = 0

        while p1 < len(str1) and p2 < len(str2):
            if str1[p1] != str2[p2]:
                return ""

            p1 += 1
            p2 += 1

        if p1 == len(str1) and p2 == len(str2):
            return str1


solution = Solution()

print("pass") if solution.gcdOfStrings("abcabc", "abc") == "abc" else print("fail")


