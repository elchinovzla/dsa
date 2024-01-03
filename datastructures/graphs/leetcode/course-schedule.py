# https://leetcode.com/problems/course-schedule/

import unittest


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if numCourses == 0:
            return True

        inDegree = []
        adjList = {}

        for i in range(numCourses):
            inDegree.append(0)
            adjList[i] = []

        for prerequisite in prerequisites:
            adjList[prerequisite[1]].append(prerequisite[0])
            inDegree[prerequisite[0]] += 1

        stack = []
        for index in range(len(inDegree)):
            if inDegree[index] == 0:
                stack.append(index)

        counter = 0
        while len(stack) > 0:
            current_node = stack.pop()
            counter += 1
            adjacent = adjList[current_node]
            for value in adjacent:
                inDegree[value] -= 1
                if inDegree[value] == 0:
                    stack.append(value)

        return counter == numCourses


class Tests(unittest.TestCase):
    def test_example1(self):
        solution = Solution()
        self.assertEqual(
            solution.canFinish(2, [[1, 0]]),
            True)

    def test_example2(self):
        solution = Solution()
        self.assertEqual(
            solution.canFinish(2, [[1, 0], [0, 1]]),
            False)

    def test_example3(self):
        solution = Solution()
        self.assertTrue(solution.canFinish(6,
                                           [[1, 0], [2, 1], [2, 5], [0, 3], [4, 3], [3, 5], [4, 5]]))


if __name__ == '__main__':
    unittest.main()
