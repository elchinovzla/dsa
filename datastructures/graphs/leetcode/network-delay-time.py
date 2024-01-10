# https://leetcode.com/problems/network-delay-time/

import unittest


class Solution(object):
    def djikstraNetworkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        distances = []
        adjList = {}

        for i in range(n):
            distances.append(float("inf"))
            adjList[i] = []

        distances[k-1] = 0
        heap = []
        heap.append(k-1)

        for i in range(len(times)):
            source = times[i][0]
            target = times[i][1]
            weight = times[i][2]

            adjList[source-1].append([target-1, weight])

        while heap:
            current_vertex = heap.pop()
            adj = adjList[current_vertex]
            for i in range(len(adj)):
                neighbour_vertex = adj[i][0]
                weight = adj[i][1]
                new_weight = distances[current_vertex] + weight
                if new_weight < distances[neighbour_vertex]:
                    distances[neighbour_vertex] = new_weight
                    heap.append(neighbour_vertex)
            heap.sort(reverse=True)

        if float("inf") in distances:
            return -1
        return max(distances)

    def bellmanFordNetworkDelayTime(self, times, n, k):
        distances = []

        for i in range(n):
            distances.append(float("inf"))

        distances[k-1] = 0

        for _ in range(n-1):
            count = 0
            for j in range(len(times)):
                source = times[j][0] - 1
                target = times[j][1] - 1
                weight = times[j][2]
                new_weight = distances[source] + weight
                if new_weight < distances[target]:
                    distances[target] = new_weight
                    count += 1
            if count < 1:
                break

        if float("inf") in distances:
            return -1
        return max(distances)


class Tests(unittest.TestCase):
    def test_example1(self):
        solution = Solution()
        self.assertEqual(
            solution.djikstraNetworkDelayTime(
                [[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2),
            2)

    def test_example2(self):
        solution = Solution()
        self.assertEqual(
            solution.djikstraNetworkDelayTime([[1, 2, 1]], 2, 1), 1)

    def test_example3(self):
        solution = Solution()
        self.assertEqual(
            solution.djikstraNetworkDelayTime([[1, 2, 1]], 2, 2), -1)

    def test_example4(self):
        solution = Solution()
        self.assertEqual(
            solution.bellmanFordNetworkDelayTime([[1, 2, 9], [3, 2, 3], [5, 3, 7], [3, 1, 5], [2, 5, -3], [4, 5, 6], [1, 4, 2], [4, 2, -4]], 5, 1), 2)


if __name__ == '__main__':
    unittest.main()
