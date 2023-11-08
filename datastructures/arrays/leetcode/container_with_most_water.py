# https://leetcode.com/problems/container-with-most-water/

import unittest


def max_area(heights):
    """
    :type height: List[int]
    :rtype: int
    """
    max_area = 0
    if len(heights) > 1:
        index_left = 0
        index_right = len(heights) - 1
        while index_left < index_right:
            new_area = min(
                heights[index_left], heights[index_right]) * (index_right-index_left)
            if new_area > max_area:
                max_area = new_area
            if heights[index_left] < heights[index_right]:
                index_left += 1
            else:
                index_right -= 1

    return max_area


class Tests(unittest.TestCase):
    def test_containerwithmostwater_example1(self):
        self.assertEqual(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)

    def test_containerwithmostwater_example2(self):
        self.assertEqual(max_area([1, 1]), 1)

    def test_containerwithmostwater_example3(self):
        self.assertEqual(max_area([4, 8, 1, 2, 3, 9]), 32)


unittest.main(exit=False)
