class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtracking(start, curr):
            ans.append(curr[:])

            for i in range(start, len(nums)):
                curr.append(nums[i])
                backtracking(i + 1, curr)
                curr.pop()

        backtracking(0, [])
        return ans