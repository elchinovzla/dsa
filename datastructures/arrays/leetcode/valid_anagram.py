# https://leetcode.com/problems/valid-anagram/
class Solution(object):
    def isAnagramWithWordCounter(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        for s_char in s:
            if s.count(s_char) != t.count(s_char):
                return False
        return True

    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)


solution = Solution()
print(solution.isAnagramWithWordCounter("anagram", "nagaram"))
print(solution.isAnagramWithWordCounter("rat", "car"))
print(solution.isAnagram("anagram", "nagaram"))
print(solution.isAnagram("rat", "car"))
