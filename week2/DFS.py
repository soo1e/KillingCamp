visited = {}
graph = {}

def dfs(cur_v):
    visited[cur_v] = True
    for next_v in graph[cur_v]:
        if next_v not in visited:
            dfs(next_v)

dfs(0)