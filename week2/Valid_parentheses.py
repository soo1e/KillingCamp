class Solution:
    def isValid(self, s: str) -> bool:
        # 기본 값 세팅
        stack = []

        # 문자열 s를 문자 단위로 순회
        for p in s:
            # 열린 괄호에 따라 대응되는 닫힌 괄호 추가
            if p == "{":
                stack.append("}")
            elif p == "[":
                stack.append("]")
            elif p == "(":
                stack.append(")")
            # 현재 문자가 닫힌 괄호 일때, 스택의 마지막 문자가 현재 문자와 같다면, pop!
            elif stack and stack[-1] == p:
                stack.pop()
            else:
                return False
        # 순회를 종료하고 stack이 비어있다면 True, 아니라면 False
        return not stack