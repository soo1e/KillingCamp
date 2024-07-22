def solution(k, dungeons):
    # 기본값 세팅
    n = len(dungeons)
    visited = [0] * n
    answer = 0

    def backtracking(k, count):
        # 최대 count를 answer에 저장
        nonlocal answer
        if count > answer:
            answer = count

        # dungeons 순회
        for i in range(n):

            # 1. 방문한 적 없고
            # 2. 현재 피로도가 던전의 필요 피로도보다 크거나 같으면
            if not visited[i] and k >= dungeons[i][0]:
                # i번째 원소 방문
                visited[i] = True
                # 백트래킹 함수 호출
                backtracking(k - dungeons[i][1], count + 1)
                # i번째 원소 pop
                visited[i] = False

    backtracking(k, 0)
    return answer

