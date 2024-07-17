from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # 기본 값 세팅
        rows, cols = len(board), len(board[0])
        # 방문한 셀을 추적하기 위한 집합
        path = set()

        # 백트래킹 함수 정의
        def backtrack(r, c, index):
            # 단어의 모든 문자를 찾았을 때
            if index == len(word):
                return True

            # 1. 현재 셀이 보드의 경계를 벗어났거나
            # 2. 현재 셀이 단어의 해당 문자와 일치하지 않거나
            # 3. 현재 셀이 이미 방문한 셀이라면 -> Return False!
            if (r < 0 or r >= rows or c < 0 or c >= cols or
                    board[r][c] != word[index] or (r, c) in path):
                return False

            # 현재 셀을 경로에 추가
            path.add((r, c))

            # 네 방향 탐색
            res = (backtrack(r + 1, c, index + 1) or
                   backtrack(r - 1, c, index + 1) or
                   backtrack(r, c + 1, index + 1) or
                   backtrack(r, c - 1, index + 1))

            # 백트래킹: 현재 셀을 경로에서 제거
            path.remove((r, c))

            return res

        # 보드 탐색 시작
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:  # 단어의 첫 문자와 같은 셀에서 탐색 시작
                    if backtrack(i, j, 0):
                        return True

        return False