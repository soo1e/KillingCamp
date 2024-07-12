from collections import deque

def solution(queue1, queue2):
    # 주어진 큐를 deque를 통해 q1, q2 생성
    q1 = deque(queue1)
    q2 = deque(queue2)

    q_size = len(q1)

    for i in range(0, 3 * q_size):
        # q1의 합이 평균과 같다면 이를 리턴한다.
        if sum(q1) == sum(q2):
            return i

        # 만약 q1의 합이 평균보다 작으면 q2에서 요소를 가져와서 더한다.
        elif sum(q1) < sum(q2):
            temp = q2.popleft()
            q1.append(temp)

        # 만약 q2의 합이 평균보다 작으면 q1에서 요소를 가져와서 더한다.
        else:
            temp = q1.popleft()
            q2.append(temp)

    # 반복문을 다 돌렸을 때 안 되면 -1을 리턴
    return -1
