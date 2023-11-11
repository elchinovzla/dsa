import unittest
# https://leetcode.com/problems/longest-substring-without-repeating-characters/


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) < 2:
            return len(s)

        longest_counter = 0
        char_map = {}
        left_pointer = 0
        for index, char in enumerate(s):
            if char in char_map:
                previously_seen_index = char_map[char]
                left_pointer = previously_seen_index + \
                    1 if previously_seen_index >= left_pointer else left_pointer
            char_map[char] = index

            longest_counter = max(longest_counter, index - left_pointer + 1)

        return longest_counter


class Tests(unittest.TestCase):
    def test_lengthOfLongestSubstring_example1(self):
        solution = Solution()
        self.assertEqual(solution.lengthOfLongestSubstring("abccabb"), 3)

    def test_lengthOfLongestSubstring_example2(self):
        solution = Solution()
        self.assertEqual(solution.lengthOfLongestSubstring("cccccc"), 1)

    def test_lengthOfLongestSubstring_example3(self):
        solution = Solution()
        self.assertEqual(solution.lengthOfLongestSubstring(""), 0)

    def test_lengthOfLongestSubstring_example4(self):
        solution = Solution()
        self.assertEqual(solution.lengthOfLongestSubstring("abcbdaac"), 4)

    def test_lengthOfLongestSubstring_example5(self):
        solution = Solution()
        self.assertEqual(solution.lengthOfLongestSubstring("a"), 1)


if __name__ == '__main__':
    unittest.main()
