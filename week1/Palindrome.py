from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []

        # 팰린드롬인지 판별하는 함수
        def is_palindrome(sub: str) -> bool:
            return sub == sub[::-1]

        # 백트래킹 함수 구현
        def backtracking(start, curr):
            # base-case : 문자열의 끝에 도달하면, 현재까지 찾은 팰린드롬 분할을 결과에 추가
            if start == len(s):
                ans.append(curr[:])
                return

            # start부터 s의 끝까지 부분 문자열을 살펴본다.
            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]

                # 부분 문자열이 팰린드롬인지 확인
                if is_palindrome(substring):
                    # 현재 부분 문자열 추가
                    curr.append(substring)

                    # 문자열의 다음 부분으로 이동
                    backtracking(end, curr)

                    # 추가한 부분 문자열 pop -> 다음 반복 준비
                    curr.pop()

        backtracking(0, [])
        return ans