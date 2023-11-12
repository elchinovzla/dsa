import unittest
# https://leetcode.com/problems/valid-palindrome-ii/


class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) < 3:
            return True

        left_index = 0
        right_index = len(s) - 1
        check__modified_sentence = False

        while left_index < right_index:
            if s[left_index] != s[right_index]:
                check__modified_sentence = True
                break
            left_index += 1
            right_index -= 1

        if not check__modified_sentence:
            return True

        left_sentence = s[0:left_index] + s[left_index+1:]
        right_sentence = s[0:right_index] + s[right_index+1:]

        return left_sentence == left_sentence[::-1] or right_sentence == right_sentence[::-1]


class Tests(unittest.TestCase):
    def test_lengthOfLongestSubstring_example1(self):
        solution = Solution()
        self.assertTrue(solution.validPalindrome(
            "raceacar"))

    def test_lengthOfLongestSubstring_example2(self):
        solution = Solution()
        self.assertTrue(solution.validPalindrome(
            "abccdba"))

    def test_lengthOfLongestSubstring_example3(self):
        solution = Solution()
        self.assertFalse(solution.validPalindrome(
            "abcdefdba"))

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
            "ab"))


if __name__ == '__main__':
    unittest.main()
