import unittest
# https://leetcode.com/problems/trapping-rain-water/


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        total_area = 0
        left_index = 0
        right_index = len(height)-1
        max_left = 0
        max_right = 0

        while left_index < right_index:
            if height[left_index] <= height[right_index]:
                if height[left_index] >= max_left:
                    max_left = height[left_index]
                else:
                    total_area += max_left-height[left_index]
                left_index += 1
            else:
                if height[right_index] >= max_right:
                    max_right = height[right_index]
                else:
                    total_area += max_right-height[right_index]
                right_index -= 1

        return total_area


class Tests(unittest.TestCase):
    def test_containerwithmostwater_example1(self):
        solution = Solution()
        self.assertEqual(solution.trap(
            [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]), 6)

    def test_containerwithmostwater_example2(self):
        solution = Solution()
        self.assertEqual(solution.trap([4, 2, 0, 3, 2, 5]), 9)

    def test_containerwithmostwater_example3(self):
        solution = Solution()
        self.assertEqual(solution.trap([0, 1, 0, 2, 1, 0, 3, 1, 0, 1, 2]), 8)

    def test_containerwithmostwater_example4(self):
        solution = Solution()
        self.assertEqual(solution.trap([]), 0)

    def test_containerwithmostwater_example5(self):
        solution = Solution()
        self.assertEqual(solution.trap([3, 4, 3]), 0)

    def test_containerwithmostwater_example6(self):
        solution = Solution()
        self.assertEqual(solution.trap([3]), 0)


if __name__ == '__main__':
    unittest.main()
