def solution(info, edges):
    # 방문을 체크할 수 있는 배열 선언
    visited = [0] * len(info)
    answer = []

    def dfs(sheep, wolf):
        # 양의 수가 늑대의 수보다 많으면 현재 양의 수를 결과 리스트에 추가
        if sheep > wolf:
            answer.append(sheep)
        else:
            return

        # Edge 탐방
        for p, c in edges:
            # 부모가 방문된 상태 & 자식이 아직 방문되지 않은 상태 -> 방문
            if visited[p] and not visited[c]:
                # 다음 노드 방문 표시
                visited[c] = True
                # 다음 노드가 양이라면 sheep + 1
                if info[c] == 0:
                    dfs(sheep + 1, wolf)
                # 다음 노드가 늑대라면 wolf + 1
                else:
                    dfs(sheep, wolf + 1)
                # 다음 노드를 방문 표시 해제
                visited[c] = False
    # 루트 노드(0번 노드)를 방문한 상태로 시작
    visited[0] = True

    # DFS 시작! -> 루트 노드가 양이므로 양의 수를 1로 시작
    dfs(1, 0)

    # 방문한 경우의 수중 가장 양을 많이 방문한 경우를 반환한다.
    return max(answer)