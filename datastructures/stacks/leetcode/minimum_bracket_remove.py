# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        orphan_open_parentese_indexes = list()
        result = []
        for index, char in enumerate(s):
            if char == ")":
                if orphan_open_parentese_indexes:
                    orphan_open_parentese_indexes.pop()
                    result.append(char)
                else:
                    result.append(" ")
            elif char != ")":
                if char == "(":
                    orphan_open_parentese_indexes.append(index)
                result.append(char)

        for i in orphan_open_parentese_indexes:
            result[i] = ""

        return "".join(result).replace(" ", "")


class Solution(object):
    # Udemy
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = list(s)
        stack = []
        for i in range(len(res)):
            if res[i] == "(":
                stack.append(i)
            elif res[i] == ")" and stack:
                stack.pop()
            elif res[i] == ")":
                res[i] = ("")

        while stack:
            res[stack.pop()] = ""

        return "".join(res)
