from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 기본 값 세팅
        cnt = 0
        row_len = len(grid)
        col_len = len(grid[0])
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        visited = [[False] * col_len for _ in range(row_len)]

        # DFS 함수 구현
        def dfs(r, c):
            visited[r][c] = True
            for i in range(4):
                next_r = r + dr[i]
                next_c = c + dc[i]
                if 0 <= next_r < row_len and 0 <= next_c < col_len:
                    if grid[next_r][next_c] == "1":
                        if visited[next_r][next_c]:
                            dfs(next_r, next_c)

        # Grid 순회
        for i in range(row_len):
            for j in range(col_len):
                # Grid의 값이 1이고 아직 방문하지 않았다면
                if grid[i][j] == "1" and not visited[i][j]:
                    # DFS를 통해 연결된 모든 1에 대해 방문 표시
                    dfs(i, j)
                    # 섬의 개수 1 증가
                    cnt += 1

        return cnt