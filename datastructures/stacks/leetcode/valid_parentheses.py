# https://leetcode.com/problems/valid-parentheses/description/

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        brackets = {
            "[": "]",
            "(": ")",
            "{": "}"
        }
        open_brackets = list()

        for char in s:
            if char in brackets.keys():
                open_brackets.append(char)
            elif not open_brackets or brackets[open_brackets.pop()] != char:
                return False
        return not open_brackets
