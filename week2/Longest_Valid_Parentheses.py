class Solution:
    def longestValidParentheses(self, s: str) -> int:

        # 스택 및 문자열의 길이 초기화
        stack = [-1]
        max_length = 0

        # 문자열 s의 각 문자와 해당 인덱스 순회
        for i, char in enumerate(s):

            # 여는 괄호인 경우, 스택에 인덱스를 추가 : 여는 괄호는 항상 새로운 시작점이 될 수 있으므로 인덱스를 저장
            if char == '(':
                stack.append(i)
            # 닫는 괄호인 경우, 스택에 가장 위의 인덱스 제거
            # 만약 스택이 비어 있는 경우, 현재 인덱스를 스택에 추가 -> 유효한 괄호가 종료되었음! -> 새로운 시작점 설정
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                # 스택이 비어있지 않은 경우 : 현재 인덱스와 스택의 맨 위 인덱스의 차이를 계산
                else:
                    max_length = max(max_length, i - stack[-1])

        return max_length