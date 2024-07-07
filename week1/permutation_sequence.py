class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        ans = []
        nums_list = []
        for i in range(1, n+1):
            nums_list.append(i)

        def backtracking(curr):
            if len(curr) == n:
                ans.append(''.join(map(str,curr)))
                return

            for num in range(len(nums_list)):
                if num not in curr:
                    curr.append(num)
                    backtracking(curr)
                    curr.pop()

        backtracking([])
        return ans[k - 1]