from collections import deque, Counter
from itertools import combinations
import sys

# 1. 백준…이니까 입력 형식에 맞춰서 인풋 값 받기
# 2. 빈 칸과 바이러스 위치 또한 입력 받기
# 3. 위의 기본 값 세팅 후 BFS or DFS 구현
# 4. 임의의 3개의 빈 칸을 선택하고 벽 세우기
# 5. 바이러스를 시작으로 상하좌우가 0이면 바이러스가 퍼질 수 있게 BFS or DFS 수행
# 6. 안전영역을 세고 만약 기존의 max값보다 크다면 갱신
# 7. 세웠던 벽을 리셋시키고 다시하기

# 입력 형식에 맞춰서 인풋 값 받기
input = sys.stdin.readline
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

# 빈 칸과 바이러스 위치 또한 입력 받기
virus, empty = [], []
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
answer = 0
for r in range(n):
    for c in range(m):
        if board[r][c] == 0:
            empty.append([r, c])
        elif board[r][c] == 2:
            virus.append([r, c])

def in_range(next_r, next_c):
    return 0 <= next_r < n and 0 <= next_c < m

# BFS 구현
def bfs():
    global answer
    tmp = [board[i][:] for i in range(n)]
    queue = deque(virus)

    while queue:
        cur_r, cur_c = queue.popleft()
        for i in range(4):
            next_r = cur_r + dr[i]
            next_c = cur_c + dc[i]
            if in_range(next_r, next_c):
                if tmp[next_r][next_c] == 0:
                    tmp[next_r][next_c] = 2
                    queue.append((next_r, next_c))

    count = Counter([])
    for row in tmp:
        count = count + Counter(row)
    answer = max(answer, count[0])
    return

# 임의의 3개의 빈 칸 선택
for new_wall in combinations(empty, 3):
    row, col = [], []
    for r, c in new_wall:
        row.append(r)
        col.append(c)
        if board[r][c] != 0:
            break
    else:
        # 선택한 3개의 빈 칸에 벽 세우기
        for i in range(3):
            board[row[i]][col[i]] = 1

        # BFS 수행
        bfs()

        # 벽 리셋
        for i in range(3):
            board[row[i]][col[i]] = 0

print(answer)