from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtracking(curr):
            # base-case : curr의 nums의 길이가 같다면 ans에 현재 만든 순열 추가
            if len(curr) == len(nums):
                ans.append(curr[:])
                return

            # list의 수 순서대로 시작 1,2,3...
            # nums를 순회
            for num in nums:
                # 현재 접근하는 정수가 curr에 없다면?
                if num not in curr:
                    # 재귀함수 호출
                    curr.append(num)
                    backtracking(curr)
                    curr.pop()

        backtracking([])
        return ans