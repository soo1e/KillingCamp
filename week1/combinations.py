class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def backtracking(start, curr):
            if len(curr) == k:
                result.append(curr[:])
                return

            for i in range(start, n + 1):  # `n`까지의 숫자 사용
                curr.append(i)
                backtracking(i + 1, curr)
                curr.pop()

        backtracking(1, [])  # 숫자는 1부터 시작
        return result
