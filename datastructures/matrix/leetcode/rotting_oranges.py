# https://leetcode.com/problems/rotting-oranges/

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row_length = len(grid)
        col_length = len(grid[0])
        timer_counter = 0
        fresh_oranges_counter = 0
        rotten_oranges = []

        for row in range(row_length):
            for col in range(col_length):
                if grid[row][col] == 2:
                    rotten_oranges.append([row, col])
                elif grid[row][col] == 1:
                    fresh_oranges_counter += 1

        queue_size = len(rotten_oranges)
        while len(rotten_oranges) > 0:
            current_rotten_orange = rotten_oranges.pop(0)
            queue_size -= 1
            row = current_rotten_orange[0]
            col = current_rotten_orange[1]

            if row - 1 >= 0 and grid[row-1][col] == 1:
                grid[row-1][col] = 2
                rotten_oranges.append([row-1, col])
                fresh_oranges_counter -= 1
            if col + 1 < col_length and grid[row][col + 1] == 1:
                grid[row][col+1] = 2
                rotten_oranges.append([row, col+1])
                fresh_oranges_counter -= 1
            if row + 1 < row_length and grid[row+1][col] == 1:
                grid[row+1][col] = 2
                rotten_oranges.append([row+1, col])
                fresh_oranges_counter -= 1
            if col - 1 >= 0 and grid[row][col-1] == 1:
                grid[row][col-1] = 2
                rotten_oranges.append([row, col-1])
                fresh_oranges_counter -= 1

            if queue_size == 0 and len(rotten_oranges) > 0:
                timer_counter += 1
                queue_size = len(rotten_oranges)

        return -1 if fresh_oranges_counter > 0 else timer_counter
