# DFS

def solution(lockers):
    # 기본 값 세팅
    visited = [False] * len(lockers)

    # DFS 함수 구현
    def dfs(cur_v):
        # 현재 방문한 노드의 방문 여부 기록
        visited[cur_v] = True

        # 현재 방에 있는 열쇠 확인
        for next_v in lockers[cur_v]:
            # 열쇠가 갈 수 있는 방의 방문 여부 확인
            if not visited[next_v]:
                # 재귀 함수 호출
                dfs(next_v)

    dfs(0)
    return all(visited)