from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 기본 값 세팅
        ans = [0] * len(temperatures)
        stack = []

        # temperatures 배열을 순회하면서 answer 배열을 채운다.
        for day, temp in enumerate(temperatures):
            # 스택이 비거나 스택의 마지막 온도가 현재 온도보다 커질 때까지 스택에서 pop하며 값을 계산
            while stack and stack[-1][1] < temp:
                prev_day = stack.pop()[0]

                # 스택에 저장해둔 해당 온도의 인덱스와 현재 인덱스를 통해 answer에 계산한 값 저장
                ans[prev_day] = day - prev_day

            # 스택에 현재 temperatures의 인덱스와 온도 저장
            stack.append((day, temp))
        return ans
