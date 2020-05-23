genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

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

    sorted_genre = sorted(sum_genres)  # 장르 정렬(오름차순)

    # 노래별 반복재생 수(idx:반복수)
    for i in range(len(genres)):
        if i not in song_cnt:
            song_cnt[i] = plays[i]

    # 노래별 장르
    for idx, val in enumerate(genres):
        song_genre[idx] = val
        # print(song_genre.values())

    final_idx = []
    final_cnt = []
    for k in range(len(sorted_genre)-1, -1, -1):
        idx_order = []
        cnt_order = []
        for song in range(len(song_genre.values())):
            if sorted_genre[k] == song_genre[song]:
                idx_order.append(song)
                cnt_order.append(song_cnt[song])
        # print(idx_order)
        # print(cnt_order)
        lst = list(zip(idx_order, cnt_order))
        print(lst)
        for c in range(len(lst)):
            # print(lst[c])
            for i in  range(1, 2):
                print(lst[c][i])

    # print(final)


    answer = []
    return answer

solution(genres, plays)
# print(solution(genres, plays))

