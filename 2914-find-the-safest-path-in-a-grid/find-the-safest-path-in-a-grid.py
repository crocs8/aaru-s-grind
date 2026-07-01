from collections import deque

class Solution(object):
    def maximumSafenessFactor(self, grid):
        n = len(grid)

        # Step 1: Multi-source BFS
        dist = [[float('inf')] * n for _ in range(n)]
        q = deque()

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dist[i][j] = 0
                    q.append((i, j))

        dirs = [(1,0),(-1,0),(0,1),(0,-1)]

        while q:
            x, y = q.popleft()

            for dx, dy in dirs:
                nx, ny = x + dx, y + dy

                if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] == float('inf'):
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))

        # Step 2: Check function
        def can(k):
            if dist[0][0] < k:
                return False

            q = deque([(0,0)])
            vis = [[False]*n for _ in range(n)]
            vis[0][0] = True

            while q:
                x, y = q.popleft()

                if x == n-1 and y == n-1:
                    return True

                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy

                    if (0 <= nx < n and 0 <= ny < n and
                        not vis[nx][ny] and
                        dist[nx][ny] >= k):

                        vis[nx][ny] = True
                        q.append((nx, ny))

            return False

        # Step 3: Binary Search
        left = 0
        right = max(max(row) for row in dist)
        ans = 0

        while left <= right:
            mid = (left + right) // 2

            if can(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans