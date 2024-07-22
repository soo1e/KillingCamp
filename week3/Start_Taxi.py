from collections import deque
import sys

# 기본 값 세팅
input = sys.stdin.readline
n, m, fuel = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
tr, tc = map(int,input().split())
tr -= 1
tc -= 1

# 승객의 출발지/도착지 저장
passenger = {}
for i in range(m):
    pr, pc, pdr, pdc = list(map(int, input().split()))
    passenger[(pr-1, pc-1)] = (pdr-1, pdc-1)

answer = 0

# 범위 적합 설정
def in_range(next_r, next_c):
    return 0 <= next_r < n and 0 <= next_c < n

def pickup(tr, tc):
    queue = deque([[tr, tc, 0]])
    visited = set([(tr, tc)])
    candidate = []
    min_distance = 1000000

    while queue:
        cur_r, cur_c, cur_d = queue.popleft()
        if cur_d > min_distance:
            break
        if (cur_r, cur_c) in passenger:
            candidate.append((cur_r, cur_c))
            min_distance = cur_d
        for dr, dc in [[-1,0],[1,0],[0,-1],[0,1]]:
            next_r, next_c, next_d = cur_r+dr, cur_c+dc, cur_d+1
            if (next_r, next_c) in visited:
                continue
            if in_range(next_r, next_c) and board[next_r][next_c] != 1:
                queue.append([next_r, next_c, next_d])
                visited.add((next_r, next_c))

    return candidate, min_distance

def go_dest(tr, tc):
    pdr, pdc = passenger[(tr, tc)]
    del passenger[(tr, tc)]
    queue = deque([[tr, tc, 0]])
    visited = set([(tr, tc)])

    while queue:
        cur_r, cur_c, cur_d = queue.popleft()
        if cur_r == pdr and cur_c == pdc:
            return cur_r, cur_c, cur_d
        for dr, dc in [[-1,0],[1,0],[0,-1],[0,1]]:
            next_r, next_c, next_d = cur_r+dr, cur_c+dc, cur_d+1
            if (next_r, next_c) in visited:
                continue
            if in_range(next_r, next_c) and board[next_r][next_c] != 1:
                queue.append([next_r, next_c, next_d])
                visited.add((next_r, next_c))
    return pdr, pdc, 10000000

# 남아있는 승객이 있다면 반복문 수행
while fuel > 0 and len(passenger) != 0:
    #✅ BFS 알고리즘 최단 거리 계산
    cand, used_fuel = pickup(tr, tc)
    if used_fuel > fuel or len(cand) == 0:
        answer = -1
        break
    # 최단거리 기준으로 가장 높은 우선순위의 승객 위치로 택시를 이동시킨다.
    tr, tc = sorted(cand)[0]
    # 연료가 충분하다면 BFS 알고리즘을 통해 승객을 도착지까지 이동시키고 연료를 보충받는다.
    fuel -= used_fuel
    pdr, pdc, used_fuel = go_dest(tr, tc)
    if used_fuel > fuel:
        answer = -1
    break
    fuel += used_fuel
    tr, tc = pdr, pdc
# 이동 성공 여부에 따라 출력값을 결정한다.
if answer == -1:
    # 승객 이동시키기에 실패한다면 -1를 출력한다.
    print(-1)
else:
    # 모든 승객 이동시키기에 성공한다면 남은 연료를 출력한다.
    print(fuel)