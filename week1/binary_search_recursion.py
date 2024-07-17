class Solution:
    def search(self, nums, target):
        def binary_search(left, right):
            # left가 right보다 크다면, -1을 반환한다.
            if left > right:
                return -1

            # left와 right의 중간 인덱스값 mid를 구한다.
            mid = (left + right) // 2

            # target이 중간값과 같다면, mid를 반환한다.
            if nums[mid] == target:
                return mid
            # target이 중간값보다 크다면,
            elif nums[mid] < target:

                # 탐색 범위를 [mid + 1, right] -> 재귀 함수 호출
                return binary_search(mid + 1, right)

            # target이 중간값보다 작으면,
            else:
                # 탐색 범위를 [left, mid - 1] -> 재귀 함수 호출
                return binary_search(left, mid - 1)

        return binary_search(0, len(nums) - 1)