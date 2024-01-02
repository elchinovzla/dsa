# https://leetcode.com/problems/all-people-report-to-the-given-manager/

import unittest


class Solution(object):
    def dfs(self, currentId, adjList, informTime):
        subordinates = adjList.get(currentId, [])
        if len(subordinates) == 0:
            return 0

        current_max_time = 0
        print(adjList, subordinates, currentId)
        for i in range(len(subordinates)):
            current_max_time = max(current_max_time, self.dfs(
                subordinates[i], adjList, informTime))

        return current_max_time + informTime[currentId]

    def allPeopleReportToTheGivenManager(self, n, headId, managers, informTime):
        def getCleanedMap(managers):
            map = {}
            for manager in managers:
                map[manager] = []
            return map

        adjList = getCleanedMap(managers)
        for employee in range(n):
            manager = managers[employee]
            if manager != -1:
                adjList[manager].append(employee)

        return self.dfs(headId, adjList, informTime)


class Tests(unittest.TestCase):
    def test_allPeopleReportToTheGivenManager_example1(self):
        solution = Solution()
        managers = [2, 2, 4, 6, -1, 4, 4, 5]
        informTime = [0, 0, 4, 0, 7, 3, 6, 0]
        number_of_nodes = 8
        self.assertEqual(
            solution.allPeopleReportToTheGivenManager(
                number_of_nodes, 4, managers, informTime),
            13)


if __name__ == '__main__':
    unittest.main()
