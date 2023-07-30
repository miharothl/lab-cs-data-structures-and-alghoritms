# https://leetcode.com/problems/reverse-words-in-a-string/

class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = s.split(' ')

        stack = []

        for i in range(len(s_list)):
            if s_list[i] != '':
                stack.append(s_list[i])

        r_list = []

        for j in range(len(stack)):
            r_list.append(stack.pop())

        return ' '.join(r_list)


solution = Solution()
print("Pass") if solution.reverseWords("the sky is blue") == "blue is sky the" else print("Fail")
print("Pass") if solution.reverseWords(" the   sky is blue") == "blue is sky the" else print("Fail")
