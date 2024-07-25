from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 기본 값 세팅
        cnt = 0
        row_len = len(grid)
        col_len = len(grid[0])
        visited = [[False] * col_len for _ in range(row_len)]

        # BFS 함수 구현
        def bfs(r, c, grid):
            # 방향
            dr = [0, 1, 0, -1]
            dc = [1, 0, -1, 0]
            visited[r][c] = True

            # 큐 생성
            q = deque()
            q.append((r, c))

            # 반복문을 통해 가는 방향이 1인지 0인지 확인
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

        # Grid 순회
        for i in range(row_len):
            for j in range(col_len):
                # 만약 Grid 값이 1이고 방문하지 않았다면
                if grid[i][j] == "1" and not visited[i][j]:
                    # BFS를 통해 연결된 모든 1에 대해 방문 표시
                    bfs(i, j, grid)
                    # 섬의 개수 1 증가
                    cnt += 1

        return cnt

