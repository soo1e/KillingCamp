from collections import deque

class Solution:
    def isBipartite(self, graph):
        n = len(graph)
        color = [-1] * n  # -1은 아직 칠해지지 않은 노드를 의미

        def bfs(start_v):
            q = deque([start_v])
            color[start_v] = 0  # 시작 노드를 0으로 칠함

            while q:
                cur_v = q.popleft()
                for next_v in graph[cur_v]:
                    if color[next_v] == -1:  # 아직 칠해지지 않은 경우
                        color[next_v] = 1 - color[cur_v]  # 다른 색으로 칠함
                        q.append(next_v)
                    elif color[next_v] == color[cur_v]:  # 이미 같은 색으로 칠해진 경우
                        return False  # 이분 그래프가 아님
            return True  # 해당 컴포넌트가 이분 그래프임

        for i in range(n):
            if color[i] == -1:  # 아직 방문하지 않은 노드에 대해 BFS 시작
                if not bfs(i):
                    return False  # 이분 그래프가 아님

        return True  # 모든 컴포넌트가 이분 그래프임