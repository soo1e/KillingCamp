from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []

        def is_palindrome(sub: str) -> bool:
            return sub == sub[::-1]

        def backtracking(start, curr):
            if start == len(s):
                ans.append(curr[:])
                return

            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]

                if is_palindrome(substring):
                    curr.append(substring)
                    backtracking(end, curr)
                    curr.pop()

        backtracking(0, [])
        return ans