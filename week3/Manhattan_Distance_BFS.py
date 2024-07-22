from collections import deque


# 유효 범위 체크
def inRange(r, c):
    return 0 <= r < 5 and 0 <= c < 5


def print_place(place):
    for row in place:
        print(row)


# (r,c)로부터 맨해튼 거리 2 이하로 앉아있는 'P'가 있으면 False 반환.
# (r,c)로부터 거리유지가 다 잘되고 있으면 True 반환
def bfs(r, c, place):
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    visited = [[False] * 5 for _ in range(5)]
    q = deque()

    # 응시자 위치의 맨해튼 거리를 0으로 초기화하여 큐에 넣고, 방문 표시를 한다.
    q.append((r, c, 0))
    visited[r][c] = True

    # 큐가 빌 때까지 반복문 수행
    while q:
        cur_r, cur_c, cur_dist = q.popleft()
        # 상하좌우 방향으로 다음 위치를 구하고, 맨해튼 거리를 1 증가

        for i in range(4):
            next_r = cur_r + dr[i]
            next_c = cur_c + dc[i]
            next_dist = cur_dist + 1
            # 다음 위치가 범위 내에 존재하고, 파티션이 아니며, 방문하지 않았을 때, 다음 코드 수행
            if (
                    inRange(next_r, next_c)
                    and place[next_r][next_c] != "X"
                    and not visited[next_r][next_c]
            ):
                # 맨해튼 거리가 2보다 크다면, 아래 과정 생략
                if next_dist > 2:
                    continue
                # 다음 위치의 맨해튼 거리가 2 이하인데, 응시자가 있다면,
                if place[next_r][next_c] == "P":
                    # 거리두기를 준수하지 않았기 때문에 False 반환
                    return False
                # 아니라면, 다음 위치와 맨해튼 거리 큐에 추가
                q.append((next_r, next_c, next_dist))
                # 다음 위치 방문 표시
                visited[next_r][next_c] = True
    # BFS를 완료했다면, 거리두기를 준수했기 때문에 True 반환
    return True


def check(place):
    for r in range(5):
        for c in range(5):
            # 현재 위치가 응시자 위치 P일 때, BFS 수행
            if place[r][c] == "P":
                # BFS 완료 후, False가 반환됐다면, 즉시 False 반환
                if not bfs(r, c, place):
                    return False
    # 대기실의 모든 위치에서 거리두기 규칙을 준수했다면, True 반환
    return True


def solution(places):
    answer = []
    # 각 대기실 별로 거리두기 준수 여부 확인
    for place in places:
        # 현재 대기실이 거리두기 규칙을 준수했다면 1 추가, 아니라면 0 추가
        if check(place):
            answer.append(1)
        else:
            answer.append(0)
    return answer
