from typing import List, Tuple


def solution(k: int, dungeons: List[Tuple[int, int]]) -> int:
    max_dungeons = [0]

    def backtracking(curr_count: int, remaining_k: int, visited: List[bool]):
        if curr_count > max_dungeons[0]:
            max_dungeons[0] = curr_count

        for i in range(len(dungeons)):
            if not visited[i] and remaining_k >= dungeons[i][0]:
                visited[i] = True
                backtracking(curr_count + 1, remaining_k - dungeons[i][1], visited)
                visited[i] = False

    backtracking(0, k, [False] * len(dungeons))
    return max_dungeons[0]

