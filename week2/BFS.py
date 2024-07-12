from collections import deque

def bfs(graph, start_v):
    q = deque()
    q.append(start_v)
    visited = {start_v : True}

    while q:
        cur_v = q.popleft()
        for next_v in graph[cur_v]:
            if next_v not in visited:
                q.append(next_v)
                visited[next_v] = True