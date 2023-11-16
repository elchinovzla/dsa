# https://leetcode.com/problems/binary-search/description/

import unittest


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left_index = 0
        right_index = len(nums)-1
        while left_index <= right_index:
            mid_index = (right_index + left_index) // 2
            if nums[mid_index] == target:
                return mid_index
            elif target > nums[mid_index]:
                left_index = mid_index + 1
            else:
                right_index = mid_index - 1

        return -1


class Tests(unittest.TestCase):
    def test_search_example1(self):
        solution = Solution()
        self.assertEqual(solution.search([-1, 0, 3, 5, 9, 12], 9), 4)

    def test_search_example2(self):
        solution = Solution()
        self.assertEqual(solution.search([-1, 0, 3, 5, 9, 12], 2), -1)

    def test_search_example2(self):
        solution = Solution()
        self.assertEqual(solution.search([-1, 0, 3, 5, 9, 12], -2), -1)


unittest.main(exit=False)
