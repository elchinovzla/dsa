# https://leetcode.com/problems/contains-duplicate/description/
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        existing_values = set()
        for value in nums:
            if value in existing_values:
                return True
            existing_values.add(value)
        return False

    def containsDuplicateUsingSort(self, nums):
        nums.sort()
        for index in range(1, len(nums)):
            if nums[index] == nums[index-1]:
                return True
        return False


solution = Solution()
print(solution.containsDuplicate([1, 2, 3, 1]))
print(solution.containsDuplicate([1, 2, 3, 4]))
print(solution.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
print(solution.containsDuplicateUsingSort([1, 2, 3, 1]))
print(solution.containsDuplicateUsingSort([1, 2, 3, 4]))
print(solution.containsDuplicateUsingSort([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
