class Solution(object):
    def countCompleteComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """

        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        ans = 0

        def dfs(node):
            visited[node] = True
            vertices = 1
            degreeSum = len(graph[node])

            for nei in graph[node]:
                if not visited[nei]:
                    v, d = dfs(nei)
                    vertices += v
                    degreeSum += d

            return vertices, degreeSum

        for i in range(n):
            if not visited[i]:
                vertices, degreeSum = dfs(i)
                edgesCount = degreeSum // 2

                if edgesCount == vertices * (vertices - 1) // 2:
                    ans += 1

        return ans