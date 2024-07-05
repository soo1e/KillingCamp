class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        found = [False]

        def backtracking(start, curr):
            if found[0]:
                return
            if len(curr) == 2:
                if nums[curr[0]] + nums[curr[1]] == target:
                    ans.extend(curr)
                    found[0] = True
                return

            for i in range(start, len(nums)):
                curr.append(i)
                backtracking(i + 1, curr)
                curr.pop()

        backtracking(0, [])
        if ans:
            return ans
        else:
            return -1