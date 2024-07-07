from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        # 유효한지 확인하기
        def is_valid(board: List[List[str]], row: int, col: int, num: str) -> bool:
            # 열이나 행에 이미 숫자가 있는지 확인하기
            for i in range(9):
                if board[row][i] == num:
                    return False  # 숫자가 현재 행에 이미 있음
                if board[i][col] == num:
                    return False  # 숫자가 현재 열에 이미 있음

            # 3x3 박스도 확인
            start_row = 3 * (row // 3)
            start_col = 3 * (col // 3)
            for i in range(3):
                for j in range(3):
                    if board[start_row + i][start_col + j] == num:
                        return False  # 숫자가 3x3 박스에 이미 있음

            return True

        def backtrack(board: List[List[str]]) -> bool:
            for row in range(9):
                for col in range(9):
                    if board[row][col] == '.': # 빈 셀 찾기
                        for num in '123456789':
                            if is_valid(board, row, col, num): # 빈 셀에 각 숫자를 넣을 수 있을지 시도
                                board[row][col] = num # True를 호출하면 만족한 것이므로 숫자를 배치
                                if backtrack(board):
                                    return True
                                board[row][col] = '.'
                        return False
            return True

        backtrack(board)
