# 반복문
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        # left가 right보다 작거나 같을 때까지 반복
        while left <= right:
            mid = left + (right - left) // 2
            # target = mid면 mid를 반환
            if nums[mid] == target:
                return mid
            # target보다 mid가 작으면
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1