from typing import List

# https://leetcode.com/problems/string-compression/

class Solution:
    def compress(self, chars: List[str]) -> int:
        p0 = 0
        p1 = 1

        if p1 == len(chars):
            no_of_repetitions = p1 - p0
            return no_of_repetitions

        s = []

        while p1 != len(chars):

            char = chars[p0]

            s.append(char)


            while chars[p0] == chars[p1]:
                if not p1 == len(chars):
                     p1 += 1

                if p1 == len(chars):
                    break

            no_of_repetitions = p1 - p0

            if no_of_repetitions > 1:
                reps = str(no_of_repetitions)
                for r in reps:
                    s.append(r)

            p0 = p1

        chars.clear()

        for i in range(len(s)):
            chars.append(s[i])
        return len(chars)



solution = Solution()

data = ["a"]
res = solution.compress(data)
print("Pass") if len(data) == 1 and data == ["a"] else print("Fail")

data = ["a","a","b","b","c","c","c"]
res = solution.compress(data)
print("Pass") if len(data) == 6 and data == ["a","2","b","2","c","3"] else print("Fail")

data = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
res = solution.compress(data)
print("Pass") if len(data) == 4 and data == ["a","b","1","2"] else print("Fail")

data = ["a","b","c"]
res = solution.compress(data)
print("Pass") if len(data) == 3 and data == ["a","b","c"] else print("Fail")

print(True)
