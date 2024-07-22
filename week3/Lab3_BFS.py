from collections import deque, Counter
from itertools import combinations
import sys

# 1. 입력 값 받기
# 2. 기본 값 세팅
# 3. 바이러스 위치 저장
# 4. 바이러스 위치 초기화
# 5. BFS 구현
# 6. BFS 수행
# 7. 인접 지점에 현재 전파 시간에 1을 더한 값으로 저장
# 8. 만약 인접 지점이 빈 칸이면 바이러스 전파 시간을 갱신하고 인접 지점이 비활성 바이러스이면 바이러스 전파 시간을 갱신하지 않는다
# 9. 최소 바이러스 전파 시간 갱신
# 10. m개의 바이러스 위치를 비활성으로 리셋
# 11. 출력

# 입력 형식에 맞춰서 인풋 값 받기
input = sys.stdin.readline
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

# 기본 값 세팅
virus = []
answer = 1000000
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# 바이러스 위치 저장
virus, empty = [], []

for r in range(n):
    for c in range(n):
        if board[r][c] == 0:
            board[r][c] = "_"
        elif board[r][c] == 1:
            board[r][c] = "-"
        elif board[r][c] == 2:
            virus.append([r, c])
            board[r][c] = '*'


# 범위 설정
def in_range(next_r, next_c):
    return 0 <= next_r < n and 0 <= next_c < n


# BFS 구현
def bfs(v):
    global answer
    queue = deque()
    for r, c in v:
        queue.append([r, c, 0])
    test_map = [board[i][:] for i in range(n)]
    max_level = 0

    while queue:
        cur_r, cur_c, level = queue.popleft()
        for i in range(4):
            next_r = cur_r + dr[i]
            next_c = cur_c + dc[i]
            next_level = level + 1

            if in_range(next_r, next_c):
                # 빈 칸이면 전파 시간 갱신
                # 빈 칸일 때 max_level 갱신하며 진행
                if test_map[next_r][next_c] == '_':
                    test_map[next_r][next_c] = next_level
                    max_level = max(max_level, next_level)
                    queue.append([next_r, next_c, next_level])

                # 인접 지점이 비활성 바이러스인 경우 -> 바이러스 전파 시간 갱신 X
                # 바이러스일 때 max_level 갱신 안 함
                elif test_map[next_r][next_c] == "*":
                    test_map[next_r][next_c] = next_level
                    queue.append([next_r, next_c, next_level])

    # 모든 칸에 바이러스가 전파가 안된 경우
    for r in range(n):
        for c in range(n):
            if test_map[r][c] == '_':
                return

    # 최소 바이러스 전파 시간을 갱신
    answer = min(answer, max_level)
    return


# 임의의 m개의 빈 칸 선택
for v in combinations(virus, m):

    # 바이러스 위치 0으로 초기화
    for r, c in v:
        board[r][c] = 0
    # BFS
    bfs(v)

    # 바이러스 위치 리셋
    for r, c in v:
        board[r][c] = '*'

# -1 반환 조건
if answer == 1000000:
    answer = -1

print(answer)
