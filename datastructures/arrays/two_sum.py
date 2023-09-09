# https://leetcode.com/problems/two-sum/description/

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        number_needed_for_target_dict = {}

        if len(nums) < 2:
            return []

        for index, number in enumerate(nums):
            number_needed_for_target = target - number
            if number_needed_for_target in number_needed_for_target_dict:
                return [number_needed_for_target_dict[number_needed_for_target], index]
            number_needed_for_target_dict[number] = index

        return []


solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))
