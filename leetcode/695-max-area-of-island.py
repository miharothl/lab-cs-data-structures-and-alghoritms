class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row_num = len(grid)
        col_num = len(grid[0])

        area = 0

        for i in range(row_num - 1):
            for j in range(col_num - 1):
                if grid[i][j] == 1:
                    grid, tmp_area = self.area(grid, i, j, 0)
                    area = max(area, tmp_area)

        return area

    def area(self, grid, row, col, area=0):

        row_num = len(grid)
        col_num = len(grid[0])

        if row < 0 or row >= row_num or col < 0 or col >= col_num or grid[row][col] == 0 or grid[row][col] == 2:
            return grid, area

        area = area + 1
        grid[row][col] = 2

        grid, area = self.area(grid, row+1, col, area)
        grid, area = self.area(grid, row-1, col, area)
        grid, area = self.area(grid, row, col+1, area)
        grid, area = self.area(grid, row, col-1, area)

        return grid, area


grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]]

solution = Solution()
print(solution.area(grid, 0, 0)[1] == 0)
print(solution.area(grid, 0, 2)[1] == 1)
print(solution.area(grid, 0, 7)[1] == 4)

assert True


print(solution.maxAreaOfIsland(grid))

print("pass") if solution.maxAreaOfIsland(grid) == 6 else print("fail")