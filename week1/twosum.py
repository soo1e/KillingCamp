from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 두 정수를 선택하기 위해 반복문을 2번 돌린다.

        # i부터 i+1, i+2... 순
        for i in range(len(nums)):
            # 동일한 i에 대해 i와 j(i+1), i와 j(i+2)... 순
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]