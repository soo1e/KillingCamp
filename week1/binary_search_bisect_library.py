# bisect 라이브러리 사용
from bisect import bisect_left

# 이진 탐색
class Solution:
    def search(self, nums, target):
        # bisect_left는 num 리스트에서 target이 삽입될 수 있는 위치 반환
        # 이를 통해 target이 위치할 수 있는 가장 왼쪽 인덱스를 찾는다.
        idx = bisect_left(nums, target)

        # idx가 nums 리스트의 길이와 같지 않고,
        # nums 리스트의 idx번째 값이 target과 같다면,
        # target이 리스트에 존재한다는 것을 의미한다.
        # 그렇기 때문에 target의 인덱스를 반환
        if idx != len(nums) and nums[idx] == target:
            return idx

        return -1