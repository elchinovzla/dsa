# https://leetcode.com/problems/number-of-islands/

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        row_length = len(grid)
        col_length = len(grid[0])
        island_counter = 0
        queue = []

        def clean():
            while queue:
                current_position = queue.pop()
                current_row = current_position[0]
                current_col = current_position[1]
                grid[current_row][current_col] = "#"

                if current_row - 1 >= 0 and grid[current_row-1][current_col] == "1":
                    queue.append([current_row-1, current_col])
                if current_col + 1 < col_length and grid[current_row][current_col + 1] == "1":
                    queue.append([current_row, current_col + 1])
                if current_row + 1 < row_length and grid[current_row+1][current_col] == "1":
                    queue.append([current_row+1, current_col])
                if current_col - 1 >= 0 and grid[current_row][current_col-1] == "1":
                    queue.append([current_row, current_col-1])

        for row in range(row_length):
            for col in range(col_length):
                if grid[row][col] == "1":
                    island_counter += 1
                    queue.append([row, col])
                    clean()

        return island_counter
