from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # 기본 값 설정
        shortest_dist = -1
        row_len = len(grid)
        col_len = len(grid[0])
        visited = [[False] * col_len for _ in range(row_len)]
        dr = [0, 1, 1, 1, 0, -1, -1, -1]
        dc = [1, 1, 0, -1, -1, -1, 0, 1]

        # grid의 시작점이 1이고 도착점이 1이면 최단거리 리턴
        if grid[0][0] == 1 or grid[row_len - 1][col_len - 1] == 1:
            return shortest_dist

        # BFS 진행할 큐 선언
        queue = deque()

        # queue(x좌표, y좌표, 거리)
        queue.append((0, 0, 1))
        visited[0][0] = True

        # BFS 진행
        while queue:
            cur_r, cur_c, cur_dist = queue.popleft()

            # 만약 도착점이라면
            if cur_r == row_len - 1 and cur_c == row_len - 1:
                shortest_dist = cur_dist
                break

            # 8방향 탐색
            for i in range(8):
                next_r = cur_r + dr[i]
                next_c = cur_c + dc[i]
                if (0 <= next_r < row_len) and (0 <= next_c < col_len):
                    if grid[next_r][next_c] == 0:
                        if not visited[next_r][next_c]:
                            queue.append((next_r, next_c, cur_dist + 1))
                            visited[next_r][next_c] = True

        return shortest_dist
