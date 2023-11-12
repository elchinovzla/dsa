import unittest
# https://leetcode.com/problems/valid-palindrome


class Solution(object):
    def isPalidrome(self, s):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        cleaned_sentence = "".join(filter(str.isalnum, str(s).lower()))
        index_left = 0
        index_right = len(cleaned_sentence) - 1
        while index_left < index_right:
            if cleaned_sentence[index_right] != cleaned_sentence[index_left]:
                return False
            index_left += 1
            index_right -= 1
        return True


class Tests(unittest.TestCase):
    def test_lengthOfLongestSubstring_example1(self):
        solution = Solution()
        self.assertTrue(solution.isPalidrome(
            "aabaa"))

    def test_lengthOfLongestSubstring_example1(self):
        solution = Solution()
        self.assertTrue(solution.isPalidrome(
            "aabbaa"))

    def test_lengthOfLongestSubstring_example1(self):
        solution = Solution()
        self.assertFalse(solution.isPalidrome(
            "abc"))

    def test_lengthOfLongestSubstring_example1(self):
        solution = Solution()
        self.assertTrue(solution.isPalidrome(
            "a"))

    def test_lengthOfLongestSubstring_example1(self):
        solution = Solution()
        self.assertTrue(solution.isPalidrome(
            ""))

    def test_lengthOfLongestSubstring_example1(self):
        solution = Solution()
        self.assertTrue(solution.isPalidrome(
            "A man, a plan, a canal: Panama"))


if __name__ == '__main__':
    unittest.main()
