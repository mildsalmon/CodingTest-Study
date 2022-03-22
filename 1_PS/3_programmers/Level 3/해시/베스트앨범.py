"""
Date    : 2022.03.23
Update  : 2022.03.23
Source  : 베스트앨범.py
Purpose : dict / 해시 / enumerate(zip) / defaultdict / lambda
url     : https://programmers.co.kr/learn/courses/30/lessons/42579
Author  : 김학진 (mildsalmon)
Email   : mildsalmon@gamil.com
"""
from collections import defaultdict


def solution(genres, plays):
    answer = []
    genres_set = set(genres)
    genre_by_play = defaultdict(int)
    genre_by_song = defaultdict(list)

    for i, (genre, play) in enumerate(zip(genres, plays)):
        genre_by_play[genre] += play
        genre_by_song[genre].append((play, i))

    for genre in genres_set:
        temp = sorted(genre_by_song[genre], key=lambda x: [-x[0], x[1]])
        genre_by_song[genre] = temp

    genres_sort = list(map(lambda x: x[0], sorted(genre_by_play.items(), key=lambda x: -x[1])))

    # print(genres_sort)
    # print(genre_by_play)
    # print(genre_by_song)

    for genre in genres_sort:
        answer.extend(list(map(lambda x: x[1], genre_by_song[genre][:2])))

    return answer

# 정확성  테스트
# 테스트 1 〉	통과 (0.02ms, 10.2MB)
# 테스트 2 〉	통과 (0.02ms, 10.2MB)
# 테스트 3 〉	통과 (0.02ms, 10.2MB)
# 테스트 4 〉	통과 (0.50ms, 10.1MB)
# 테스트 5 〉	통과 (0.07ms, 10.2MB)
# 테스트 6 〉	통과 (0.06ms, 10.2MB)
# 테스트 7 〉	통과 (0.05ms, 10.3MB)
# 테스트 8 〉	통과 (0.03ms, 10.2MB)
# 테스트 9 〉	통과 (0.02ms, 10.3MB)
# 테스트 10 〉	통과 (0.08ms, 10.1MB)
# 테스트 11 〉	통과 (0.03ms, 10.3MB)
# 테스트 12 〉	통과 (0.04ms, 10.3MB)
# 테스트 13 〉	통과 (0.07ms, 10.2MB)
# 테스트 14 〉	통과 (0.07ms, 10.3MB)
# 테스트 15 〉	통과 (0.02ms, 10.2MB)
#
# 채점 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0