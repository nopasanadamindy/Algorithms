from operator import itemgetter
from collections import deque

genres = ["classic", "pop", "classic", "classic"]
plays = [500, 600, 150, 800]

def solution(genres, plays):
    sum_genres = {} # 장르별 합
    song_cnt = {}  #노래별 재생 수
    song_genre = {} # 노래별 장르
    # 장르 우선순위(sorted_genre 오름차순)
    for genre in range(len(genres)):
        if genres[genre] not in sum_genres:
            sum_genres[genres[genre]] = plays[genre]
        else:
            sum_genres[genres[genre]] += plays[genre]
    # print(sum_genres)
    sorted_genre = sorted(sum_genres)  # 장르 정렬(오름차순)
    # print(sorted_genre)

    # 노래별 반복재생 수(idx:반복수)
    for i in range(len(genres)):
        if i not in song_cnt:
            song_cnt[i] = plays[i]
    # print(song_cnt)

    # # 노래별 장르
    for idx, val in enumerate(genres):
        song_genre[idx] = val
    answer = []
    for k in range(len(sorted_genre)-1, -1, -1):
        idx_order = []
        cnt_order = []
        for song in range(len(song_genre.values())):
            if sorted_genre[k] == song_genre[song]:
                idx_order.append(song)
                cnt_order.append(song_cnt[song])
        lst = list(zip(idx_order, cnt_order))
        lst = sorted(lst, key=itemgetter(1), reverse=True)

        q = deque(maxlen=2)
        for listing in lst:
            q.append(listing)

        for a in range(len(q)):
            answer.append(lst[a][0])
    return answer
# (solution(genres, plays))
print(solution(genres, plays))

