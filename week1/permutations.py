class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtracking(curr):
            if len(curr) == len(nums):
                ans.append(curr[:])
                return

            for num in nums:
                if num not in curr:
                    curr.append(num)
                    backtracking(curr)
                    curr.pop()

            ans = []
            backtracking([])
            return ans