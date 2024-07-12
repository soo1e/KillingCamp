def trap(height):

    # 투 포인터 사용을 위해 왼쪽, 오른쪽 지정
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    water_trapped = 0

    # 각 포인터에서 높이 값을 비교하면서 더 낮은 쪽의 포인터를 움직인다.
    while left < right:
        if left_max < right_max:
            left = left + 1
            left_max = max(left_max, height[left])

            # 현재 높이와 포인터가 움직이는 쪽의 최대 높이 값 사이의 차이만큼 물이 고인다고 계산
            water_trapped += left_max - height[left]
        else:
            right = right - 1
            right_max = max(right_max, height[right])
            water_trapped += right_max - height[right]

    return water_trapped
