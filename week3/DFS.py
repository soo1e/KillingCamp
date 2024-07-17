def isValid(r,c):
    # 가장자리 부분에서는 옆이나 위와 같이 다른 방향으로 나가면 밖으로 나가지기 때문에 범위를 설정
    # grid[r][c] == 1은 vertex가 1이다. 즉, 1만 찾아서 다닐거다!
    return 0 <= r < row_len and 0 <= c < col_len and grid[r][c] == 1

def dfs(r,c):
    visited[r][c] = True
    for i in range(4):
        next_r = r + dr[i]
        next_c = c + dc[i]
        if isValid(next_r, next_c):
            if not visited[next_r][next_c]:
                dfs(next_r, next_c)


grid = [...]
row_len, col_len = len(grid), len(grid[0])
visited = [[False] * col_len for _ in range(row_len)]
dr = [0,1,0,1]
dc = [1,0,1,0]
dfs(0,0)