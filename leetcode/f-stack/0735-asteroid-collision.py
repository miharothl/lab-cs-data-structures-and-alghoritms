# https://leetcode.com/problems/asteroid-collision
from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack = []
        for asteroid in asteroids:
            while stack and stack[-1] > 0 and asteroid < 0:
                if stack[-1] + asteroid < 0:
                    stack.pop()
                elif stack[-1] + asteroid > 0:
                    break
                else:
                    stack.pop(); break
            else:
                stack.append(asteroid)
        return stack

        # stack = []
        # for asteroid in asteroids:
        #
        #     destroyed = False
        #     if asteroid < 0:
        #         # check of collision
        #         while stack and stack[-1] > 0 and stack[-1] < abs(asteroid):
        #             if stack[-1] == abs(asteroid):
        #                 destroyed = True
        #             stack.pop()
        #
        #         if not destroyed:
        #             if not stack or stack[-1] < 0:
        #                 stack.append(asteroid)
        #
        #     else:
        #         stack.append(asteroid)
        #
        # return stack

    # def asteroidCollision(self, asteroids: List[int]) -> List[int]:
    #
    #     stack = []
    #
    #     for i in range(len(asteroids)):
    #         if asteroids[i] > 0:
    #             stack.append(asteroids[i])
    #         elif len(stack) == 0 or stack[len(stack) - 1] < 0:
    #             stack.append(asteroids[i])
    #         else:
    #             # check collision
    #             while len(stack) > 0 and stack[len(stack) - 1] > 0:
    #
    #                 a1 = stack[len(stack) - 1]
    #                 a2 = asteroids[i]
    #
    #                 if a1 > abs(a2):
    #                     break
    #                 elif a1 < abs(a2):
    #                     stack.pop()
    #                 else:
    #                     stack.pop()
    #                     break
    #
    #             if len(stack) > 0 and stack[len(stack) - 1] < 0:
    #                 stack.append(asteroids[i])
    #
    #     return stack


solution = Solution()
print("Pass") if solution.asteroidCollision([5, 10, -5]) == [5, 10] else print("Fail")
print("Pass") if solution.asteroidCollision([8, -8]) == [] else print("Fail")
print("Pass") if solution.asteroidCollision([10, 2, -5]) == [10] else print("Fail")
print("Pass") if solution.asteroidCollision([-2, -1, 1, 2]) == [-2, -1, 1, 2] else print("Fail")
print("Pass") if solution.asteroidCollision([-2, -2, 1, -2]) == [-2, -2, -2] else print("Fail")
print("Pass") if solution.asteroidCollision([-2, -2, 1, -1]) == [-2, -2] else print("Fail")
print("Pass") if solution.asteroidCollision([-2, 1, 1, -1]) == [-2, 1] else print("Fail")
