from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0
        row_len = len(grid)
        col_len = len(grid[0])
        visited = [[False] * col_len for _ in range(row_len)]

        def bfs(r, c, grid):
            dr = [0, 1, 0, -1]
            dc = [1, 0, -1, 0]
            visited[r][c] = True
            q = deque()
            q.append((r, c))
            while q:
                cur_r, cur_c = q.popleft()
                for i in range(4):
                    next_r = cur_r + dr[i]
                    next_c = cur_c + dc[i]
                    if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
                        if grid[r][c] == "1":
                            if visited[next_r][next_c]:
                                visited[next_r][next_c] = True
                                q.append((next_r, next_c))

        for i in range(row_len):
            for j in range(col_len):
                if grid[i][j] == "1" and not visited[i][j]:
                    bfs(i, j, grid)
                    cnt += 1

        return cnt

