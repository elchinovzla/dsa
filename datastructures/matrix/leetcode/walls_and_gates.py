# https://leetcode.com/problems/walls-and-gates/

import unittest

WALL = -1
GATE = 0
EMPTY = 2147483647


class Solution(object):

    def wallsAndGates(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        row_length = len(grid)
        col_length = len(grid[0])

        def update_grid(row, col, counter):
            if row >= row_length or row < 0 or col >= col_length or col < 0:
                return
            elif counter > grid[row][col]:
                return

            grid[row][col] = counter
            counter += 1
            update_grid(row+1, col, counter)
            update_grid(row, col+1, counter)
            update_grid(row-1, col, counter)
            update_grid(row, col-1, counter)

        for row in range(row_length):
            for col in range(col_length):
                if grid[row][col] == GATE:
                    update_grid(row, col, 0)

        return grid


class Tests(unittest.TestCase):
    def test_wallsAndGates_example1(self):
        solution = Solution()
        global EMPTY, WALL, GATE
        initial_matrix = [
            [EMPTY, WALL, GATE, EMPTY],
            [EMPTY, EMPTY, EMPTY, WALL],
            [EMPTY, WALL, EMPTY, WALL],
            [GATE, WALL, EMPTY, EMPTY]
        ]
        expected_matrix = [
            [3, WALL, GATE, 1],
            [2, 2, 1, WALL],
            [1, WALL, 2, WALL],
            [GATE, WALL, 3, 4]
        ]
        self.assertEqual(solution.wallsAndGates(
            initial_matrix), expected_matrix)

    def test_wallsAndGates_example2(self):
        solution = Solution()
        global EMPTY, WALL, GATE
        initial_matrix = [
            [EMPTY, GATE],
            [EMPTY, EMPTY]
        ]
        expected_matrix = [
            [1, GATE],
            [2, 1]
        ]
        self.assertEqual(solution.wallsAndGates(
            initial_matrix), expected_matrix)


unittest.main(exit=False)
