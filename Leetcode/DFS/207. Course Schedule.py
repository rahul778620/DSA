# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
#  You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates
#   that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.


# Example 1:

# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take.
# To take course 1 you should have finished course 0. So it is possible.
# Example 2:

# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take.
# To take course 1 you should have finished course 0, and to take course 0 you should
# also have finished course 1. So it is impossible.

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        for cur, pre in prerequisites:
            preMap[cur].append(pre)
        visited = set()

        def dfs(crs):
            if crs in visited:
                return False
            if preMap[crs] == []:
                return True
            visited.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            preMap[crs] = []
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True


##############################################################
# Topologival sort

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for i in range(numCourses)]
        degree = [0] * numCourses   # in-degree

        for after, before in prerequisites:
            adj[before].append(after)
            degree[after] += 1

        queue = set([node for node in range(numCourses) if degree[node] == 0])
        # initialize queues with every node that has no parent
        nodesPopped = 0

        while len(queue) > 0:
            node = queue.pop()
            nodesPopped += 1

            for child in adj[node]:
                degree[child] -= 1
                if degree[child] == 0:
                    queue.add(child)

        return nodesPopped == numCourses
