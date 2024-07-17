from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtracking(start, curr):
            # 부분집합 -> 모든 요소에 대해서 on/off
            # 따라서 모든 과정을 append
            ans.append(curr[:])

            # nums의 마지막 인덱스까지 순회
            for i in range(start, len(nums)):
                # 재귀함수 호출
                curr.append(nums[i])
                backtracking(i + 1, curr)
                curr.pop()

        backtracking(0, [])
        return ans