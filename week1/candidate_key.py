from itertools import combinations
from typing import List

def solution(relation: List[List[str]]) -> int:
    row_len = len(relation)
    col_len = len(relation[0])
    candidate_keys = []

    # 모든 속성의 조합을 생성 (1개부터 col_len개까지)
    for i in range(1, col_len + 1):
        for comb in combinations(range(col_len), i):
            # comb 조합에 대해 유일성 확인
            if is_unique(comb, relation):
                # 최소성을 만족하는지 확인
                if is_minimal(comb, candidate_keys):
                    candidate_keys.append(comb)

    return len(candidate_keys)

def is_unique(comb, relation):
    seen = set()
    for row in relation:
        # comb 조합으로 생성된 튜플을 확인
        key = tuple(row[idx] for idx in comb)
        if key in seen:
            return False
        seen.add(key)
    return True

def is_minimal(comb, candidate_keys):
    for key in candidate_keys:
        # 이미 있는 후보 키의 부분 집합이면 최소성을 만족하지 않음
        if set(key).issubset(comb):
            return False
    return True
