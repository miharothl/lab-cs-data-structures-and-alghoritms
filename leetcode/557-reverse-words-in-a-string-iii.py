class Solution(object):

    def reverseWord(self, s, pl, ph):

        while pl < ph:
            tmp = s[pl]
            s[pl] = s[ph]
            s[ph] = tmp
            pl += 1
            ph -= 1

        return s

    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        array = list(s)

        p = 0
        for i in range(len(array)):
            if array[i] == ' ':
                self.reverseWord(array, p, i - 1)
                p = i + 1

        self.reverseWord(array, p, len(array)-1)

        ret = ''
        for item in array:
            ret += item

        return ret

solution = Solution()
print(solution.reverseWords("Let's take LeetCode contest"))
# print("pass") if solution.reverseWords("Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc" else print("fail")
