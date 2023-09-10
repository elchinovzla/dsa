# https://leetcode.com/problems/rotate-array/description/

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        steps_back_without_cycling = k % len(nums)
        new_first_index = len(nums) - steps_back_without_cycling
        result = []
        for index in range(new_first_index, len(nums)):
            result.append(nums[index])
        for index in range(0, new_first_index):
            result.append(nums[index])
        for index, new_value in enumerate(result):
            nums[index] = new_value
        print(nums)

    def efficient_rotate(self, nums, k):
        si = len(nums) - (k % len(nums))
        nums[:] = nums[si:] + nums[0:si]
        print(nums)


solution = Solution()
solution.rotate([1, 2, 3, 4, 5, 6, 7], 3)
solution.rotate([-1, -100, 3, 99], 2)
solution.rotate([1, 2], 3)
solution.efficient_rotate([1, 2, 3, 4, 5, 6, 7], 3)
solution.efficient_rotate([-1, -100, 3, 99], 2)
solution.efficient_rotate([1, 2], 3)
