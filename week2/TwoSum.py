from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 원본 리스트의 값과 인덱스를 튜플로 저장
        indexed_nums = [(num, idx) for idx, num in enumerate(nums)]

        # 값만 정렬하여 사용하기 위한 리스트
        sorted_nums = sorted(indexed_nums, key=lambda x: x[0])

        l, r = 0, len(sorted_nums) - 1

        # 왼쪽 포인터가 오른쪽 포인터보다 작을 동안 반복한다.
        while l < r:
            current_sum = sorted_nums[l][0] + sorted_nums[r][0]

            if current_sum < target:
                l += 1
            elif current_sum > target:
                r -= 1
            else:

                # 원본 리스트에서의 인덱스를 반환
                return [sorted_nums[l][1], sorted_nums[r][1]]

        # 솔루션이 보장되지 않는다면 빈 리스트를 반환
        return []