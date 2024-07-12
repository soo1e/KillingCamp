def solution(lockers):
    visited = [False] * len(lockers)

    def dfs(cur_v):
        visited[cur_v] = True
        for next_v in lockers[cur_v]:
            if not visited[next_v]:
                dfs(next_v)

    dfs(0)
    return all(visited)