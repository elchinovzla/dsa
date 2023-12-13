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

        def check_oranges():
            oranges = {
                "rotten": [],
                "fresh": []
            }

            for row in range(row_length):
                for col in range(col_length):
                    if grid[row][col] == 2:
                        oranges["rotten"].append([row, col])
                    elif grid[row][col] == 1:
                        oranges["fresh"].append([row, col])

            return oranges

        def rot_nearby_oranges(row, col):
            has_an_orange_rot = False
            if row - 1 >= 0 and grid[row-1][col] == 1:
                grid[row-1][col] = 2
                has_an_orange_rot = True
            if col + 1 < col_length and grid[row][col + 1] == 1:
                grid[row][col+1] = 2
                has_an_orange_rot = True
            if row + 1 < row_length and grid[row+1][col] == 1:
                grid[row+1][col] = 2
                has_an_orange_rot = True
            if col - 1 >= 0 and grid[row][col-1] == 1:
                grid[row][col-1] = 2
                has_an_orange_rot = True

            return has_an_orange_rot

        def check_rotten_oranges(rotten_oranges, timer_counter):
            has_an_orange_rot = False
            while rotten_oranges:
                current_position = rotten_oranges.pop()
                current_row = current_position[0]
                current_col = current_position[1]
                grid[current_row][current_col] = -1
                has_a_new_orange_rot = rot_nearby_oranges(
                    current_row, current_col)
                has_an_orange_rot = has_an_orange_rot or has_a_new_orange_rot

            return timer_counter + 1 if has_an_orange_rot else timer_counter

        oranges = check_oranges()
        rotten_oranges = oranges.get("rotten")
        fresh_oranges = oranges.get("fresh")

        while rotten_oranges:
            timer_counter = check_rotten_oranges(rotten_oranges, timer_counter)
            oranges = check_oranges()
            rotten_oranges = oranges.get("rotten")
            fresh_oranges = oranges.get("fresh")

        print(rotten_oranges, fresh_oranges, timer_counter)

        return -1 if len(fresh_oranges) > 0 else timer_counter
