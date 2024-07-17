from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def backtracking(start, curr):
            # k와 길이가 같다면 ans에 추가
            if len(curr) == k:
                ans.append(curr[:])
                return

            # start부터 n까지 순회
            for i in range(start, n + 1):  # `n`까지의 숫자 사용

                # 재귀 함수 호출
                curr.append(i)
                backtracking(i + 1, curr)
                curr.pop()

        backtracking(1, [])  # 숫자는 1부터 시작
        return ans