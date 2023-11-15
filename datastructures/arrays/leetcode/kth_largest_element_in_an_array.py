# https://leetcode.com/problems/kth-largest-element-in-an-array/

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        self.quick_select(nums, 0, len(nums)-1, len(nums)-k)
        return nums[-k]

    def quick_select(self, nums, left_index, right_index, index_to_find):
        if left_index < right_index:
            partition_index = self.partition(nums, left_index, right_index)
            if partition_index == index_to_find:
                exit
            elif index_to_find < partition_index:
                self.quick_select(nums, left_index,
                                  partition_index - 1, index_to_find)
            else:
                self.quick_select(nums, partition_index+1,
                                  right_index, index_to_find)

    def partition(self, nums, left_index, right_index):
        pivot = nums[right_index]
        partition_index = left_index
        for i in range(left_index, right_index):
            if nums[i] < pivot:
                nums[i], nums[partition_index] = nums[partition_index], nums[i]
                partition_index += 1
        nums[partition_index], nums[right_index] = nums[right_index], nums[partition_index]
        return partition_index
