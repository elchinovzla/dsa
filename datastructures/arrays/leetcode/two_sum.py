# https://leetcode.com/problems/two-sum/description/

import unittest


def two_sum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    target_indexes = {}

    if len(nums) < 2:
        return []

    for index, number in enumerate(nums):
        number_needed_for_target = target - number
        if number_needed_for_target in target_indexes:
            return [target_indexes[number_needed_for_target], index]
        target_indexes[number] = index

    return []


class Tests(unittest.TestCase):
    def test_twosum_answerwithinfirstindexes_returnsfirstindexes(self):
        self.assertEqual(two_sum([2, 7, 11, 15], 9), [0, 1])

    def test_twosum_answerwithinlast_indexes_returnslastindexes(self):
        self.assertEqual(two_sum([1, 3, 7, 9, 2], 11), [3, 4])

    def test_twosum_emptyarray_returnsempty(self):
        self.assertEqual(two_sum([], 5), [])

    def test_twosum_arraytoosmall_returnsempty(self):
        self.assertEqual(two_sum([5], 11), [])

    def test_twosum_arraydonothavevalues_returnsempty(self):
        self.assertEqual(two_sum([1, 2, 5, 4], 19), [])


unittest.main(exit=False)
