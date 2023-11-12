import unittest
# https://leetcode.com/problems/valid-palindrome


class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
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
        self.assertTrue(solution.validPalindrome(
            "aabaa"))

    def test_lengthOfLongestSubstring_example2(self):
        solution = Solution()
        self.assertTrue(solution.validPalindrome(
            "aabbaa"))

    def test_lengthOfLongestSubstring_example3(self):
        solution = Solution()
        self.assertFalse(solution.validPalindrome(
            "abc"))

    def test_lengthOfLongestSubstring_example4(self):
        solution = Solution()
        self.assertTrue(solution.validPalindrome(
            "a"))

    def test_lengthOfLongestSubstring_example5(self):
        solution = Solution()
        self.assertTrue(solution.validPalindrome(
            ""))

    def test_lengthOfLongestSubstring_example6(self):
        solution = Solution()
        self.assertTrue(solution.validPalindrome(
            "A man, a plan, a canal: Panama"))


if __name__ == '__main__':
    unittest.main()
