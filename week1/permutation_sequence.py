from typing import List
from math import factorial

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # 초기화: 숫자 리스트와 k를 0 인덱스 기반으로 변환
        nums = list(range(1, n + 1))
        k = k - 1  # 1,2,3...에서 0,1,2,3... 로 변환

        # 결과 문자열 초기화
        result = []

        # 모든 자리수에 대해 계산
        for i in range(n):

            # 현재 자리에서 올 숫자의 인덱스 계산

            # 현재 자리에서 남은 숫자들의 순열 개수 계산
            fact = factorial(n - 1 - i)

            # 인덱스 계산
            index = k // fact
            k %= fact

            # 결과에 숫자를 추가하고 리스트에서 제거
            result.append(str(nums[index]))
            nums.pop(index)

        return ''.join(result)