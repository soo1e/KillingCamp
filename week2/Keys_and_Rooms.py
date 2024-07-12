from collections import deque
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # 방문 리스트 초기화
        visited = [False] * len(rooms)

        # BFS 정의
        def bfs(rooms, start_v, visited):
            # Queue 생성
            q = deque()

            # 시작점을 Queue에 등록 후 방문 목록에 이에 해당하는 인덱스 초기화
            q.append(start_v)
            visited[start_v] = True

            # Queue에 요소가 있는 동안은 계속 반복
            while q:
                # 현재의 점을 Queue에서 가장 먼저 들어온 친구 등록 및 제거
                cur_v = q.popleft()

                # rooms 리스트의 현재 요소에 이어진 친구들을 반복문을 통해서 사용
                for next_v in rooms[cur_v]:

                    # 만약 방문 리스트에 해당 방을 방문한 적이 없으면 Queue에 추가하고 방문 기록을 True로 바꿔준다.
                    if not visited[next_v]:
                        q.append(next_v)
                        visited[next_v] = True

            # False가 존재한다면 False
            if False in visited:
                return False

            # 그렇지 않다면 모든 방을 방문 할 수 있다는 말이므로 True
            else:
                return True
        bfs(rooms, 0, visited)
        return all(visited)