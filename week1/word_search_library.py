import itertools
from collections import Counter


def can_form_word(word, board):
    # 주어진 word에 있는 각 문자의 빈도수를 계산 후 딕셔너리 형태로 저장
    word_dict = Counter(word)

    # 보드에 있는 모든 문자의 빈도수를 계산하여 딕셔너리 형태로 저장
    # itertools.chain.from_iterable(board)는 2차원 리스트 'board'를 1차원으로 평탄화
    board_dict = Counter(itertools.chain.from_iterable(board))

    # word에 있는 각 문자의 빈도수 > board에 있는 해당 문자의 빈도수 -> word를 보드에서 만들 수 없으므로 False 반환
    if any(count > board_dict[char] for char, count in word_dict.items()):
        return False

    # 단어 방향 최적화
    if word_dict[word[0]] > word_dict[word[-1]]:
        word = word[::-1]

    # 추가적인 단어 찾기 논리를 여기에 추가

    return True  # 예시로 True 반환, 실제로는 단어 찾기 논리에 따라 결과 반환

board = [
    ['n', 'o', 'n', 'e'],
    ['e', 'x', 'a', 'm'],
    ['p', 'l', 'e', 's'],
    ['t', 'e', 's', 't']
]
