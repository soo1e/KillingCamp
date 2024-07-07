from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # 보드 생성
        def create_board(state: List[int]) -> List[str]:
            # 보드 초기화
            board = []
            for i in range(n):
                row = ['.'] * n
                # state 리스트 값에 따라 현재 행의 특정 위치에 퀸 배치
                row[state[i]] = 'Q'
                # 문자열로 변환
                board.append(''.join(row))
            return board

        def backtrack(row: int):
            # Base Case : row가 n에 도달할 때
            if row == n:
                solutions.append(create_board(state))
                return

            # 열과 대각선의 유효성 검사
            for col in range(n):
                if col in columns or (row - col) in diag1 or (row + col) in diag2:
                    continue

                # 퀸 배치
                state[row] = col
                columns.add(col)

                # 퀸의 현재 위치를 대각선 집합에 추가하여 추적
                diag1.add(row - col)
                diag2.add(row + col)

                # 다음 행 탐색
                backtrack(row + 1)

                # 퀸 제거
                columns.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        # 보드 상태 추적
        solutions = []
        state = [-1] * n
        columns = set()
        diag1 = set()
        diag2 = set()

        backtrack(0)
        return solutions