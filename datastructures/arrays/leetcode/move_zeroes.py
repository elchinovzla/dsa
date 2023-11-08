# https://leetcode.com/problems/move-zeroes/description/

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 1:
            return []
        non_zero_index = 0
        for number in (nums):
            if number != 0:
                nums[non_zero_index] = number
                non_zero_index += 1

        while non_zero_index < len(nums):
            nums[non_zero_index] = 0
            non_zero_index += 1
        return nums


solution = Solution()
print(solution.moveZeroes([0, 1, 0, 3, 12]))
print(solution.moveZeroes([0, 0, 1]))
