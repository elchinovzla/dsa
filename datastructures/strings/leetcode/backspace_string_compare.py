import unittest
# https://leetcode.com/problems/backspace-string-compare/


class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def clean(sentence):
            result = []
            for char in sentence:
                if char != '#':
                    result.append(char)
                elif result:
                    result.pop()
            return result

        return clean(s) == clean(t)


class Tests(unittest.TestCase):
    def test_backspaceCompare_example1(self):
        solution = Solution()
        self.assertTrue(solution.backspaceCompare("ab#z", "az#z"))

    def test_backspaceCompare_example2(self):
        solution = Solution()
        self.assertFalse(solution.backspaceCompare("abc#d", "acc#c"))

    def test_backspaceCompare_example3(self):
        solution = Solution()
        self.assertTrue(solution.backspaceCompare("x#y#z#", "a#"))

    def test_backspaceCompare_example4(self):
        solution = Solution()
        self.assertTrue(solution.backspaceCompare("a###b", "b"))

    def test_backspaceCompare_example5(self):
        solution = Solution()
        self.assertFalse(solution.backspaceCompare("Ab#z", "ab#z"))

    def test_backspaceCompare_example6(self):
        solution = Solution()
        self.assertTrue(solution.backspaceCompare("a##c", "#a#c"))

    def test_backspaceCompare_example7(self):
        solution = Solution()
        self.assertFalse(solution.backspaceCompare("bbbextm", "bbb#extm"))

    def test_backspaceCompare_example8(self):
        solution = Solution()
        self.assertTrue(solution.backspaceCompare("###############", "##"))


if __name__ == '__main__':
    unittest.main()
