### 재귀 (백트래킹)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        def backtracking(start, ans):
            # base-case : ans에 2개의 원소만 포함되어 있다면
            if len(ans) == 2:
                # 두 정수의 합이 target과 같다면, ans를 반환
                if nums[ans[0]] + nums[ans[1]] == target:
                    return ans
                return False
            # start부터 마지막 원소 인덱스까지 순회
            for i in range(start, len(nums)):
                ans.append(i)
                result = backtracking(i + 1, ans)
                if result:
                    return result
                ans.pop()
            return False

        return backtracking(0, [])