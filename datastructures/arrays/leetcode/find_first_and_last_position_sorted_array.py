# https://leetcode.com/problems/binary-search/description/

import unittest


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        first_found_index = self.binary_search(nums, 0, len(nums)-1, target)
        if first_found_index != -1:
            lower_found_index = first_found_index
            upper_found_index = first_found_index

            temp_lower = lower_found_index
            while temp_lower != -1:
                temp_lower = self.binary_search(
                    nums, 0, lower_found_index-1, target)
                if temp_lower != -1:
                    lower_found_index = temp_lower

            temp_upper = upper_found_index
            while temp_upper != -1:
                temp_upper = self.binary_search(
                    nums, upper_found_index+1, len(nums)-1, target)
                if temp_upper != -1:
                    upper_found_index = temp_upper

            return [lower_found_index, upper_found_index]
        return [-1, -1]

    def binary_search(self, nums, left_index, right_index, target):
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
        self.assertEqual(solution.searchRange([5, 7, 7, 8, 8, 10], 8), [3, 4])

    def test_search_example2(self):
        solution = Solution()
        self.assertEqual(solution.searchRange(
            [-5, 7, 7, 8, 8, 10], 6), [-1, -1])

    def test_search_example3(self):
        solution = Solution()
        self.assertEqual(solution.searchRange([], 0), [-1, -1])

    def test_search_example4(self):
        solution = Solution()
        self.assertEqual(solution.searchRange(
            [1, 3, 3, 5, 5, 5, 5, 9], 5), [3, 6])


unittest.main(exit=False)
