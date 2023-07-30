from typing import List

# https://www.youtube.com/watch?v=VuiXOc81UDM

class Solution:

    def dfs(self, grid, row, col, old_color, new_color):

        row_num = len(grid)
        col_num = len(grid[0])

        # print("{} {}".format(row, col))

        if row < 0 or row > row_num - 1 or col < 0 or col > col_num - 1 or grid[row][col] != old_color:
            return grid
        else:

            grid[row][col] = new_color

            grid = self.dfs(grid, row + 1, col, old_color, new_color)
            grid = self.dfs(grid, row - 1, col, old_color, new_color)
            grid = self.dfs(grid, row, col + 1, old_color, new_color)
            grid = self.dfs(grid, row, col - 1, old_color, new_color)

        # grid[row][col] = new_color
        return grid

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        if image[sr][sc] == color:
            return image
        else:
            self.dfs(image, sr, sc, image[sr][sc], color)

        return image

image = [[1, 1, 1],
         [1, 1, 0],
         [1, 0, 1]]
sr = 1
sc = 1
color = 2

solution = Solution()

print("pass") if solution.floodFill([[1, 1, 1],
                                     [1, 1, 0],
                                     [1, 0, 1]], sr, sc, color) == [[2,2,2],
                                                                    [2,2,0],
                                                                    [2,0,1]] else print("fail")
print("pass") if solution.floodFill([[0, 1, 1],
                                     [1, 1, 0],
                                     [1, 0, 1]], sr, sc, color) == [[0,2,2],
                                                                    [2,2,0],
                                                                    [2,0,1]] else print("fail")
print("pass") if solution.floodFill([[0, 0, 0],
                                     [0, 0, 0],
                                     [0, 0, 0]], sr, sc, 0) == [[0, 0, 0],
                                                                [0, 0, 0],
                                                                [0, 0, 0]] else print("fail")