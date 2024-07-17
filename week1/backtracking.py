class Solution:
    def forBacktracking(self, curr):
        ans = []
        def backtracking(start, curr):
            # Base-Case
                # return

            for i in range(start, n+1):
                curr.append(i)
                backtracking(i+1, curr)
                curr.pop()

        backtracking()