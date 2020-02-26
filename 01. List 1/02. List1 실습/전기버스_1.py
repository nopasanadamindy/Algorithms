def find(power):
    last = 0 + K   # 0 다음부터 시작
    cnt = 0
    while last < N:    # 도착보다 작은 동안에
        # 충전소 있으면 cnt 증가
        if power[last]:
            cnt += 1
        # 충전소 없으면 충전기를 찾을 때 까지 이동 위치를 K-1, K-2처럼 하나씩 줄여감
        # 만약 K=0이 되면 종점에 도착할 수 없는 경우임
        else:
            i = 0
            flag = 0   # 0: 충전기 없음, 1: 충전기 있음
            while i < K and last-i > 0: #K 범위와 last-i가 양수일 때
                if power[last-i] :
                    last -= i
                    cnt += 1
                    flag = 1
                    break
                i += 1

            if flag == 0:
                return 0
        last += K

    return cnt


import sys
sys.stdin = open("전기버스_input.txt")

T = int(input())
for tc in range(T):
    # K : 한번 충전으로 이동할 수 있는 정류장 수
    # N : 정류장 수
    # M : 충전기 설치된 정류장 번호
    K, N, M = map(int, input().split())  #1 ≤ K, N, M ≤ 100
    power = [0] * (N+1) # 마지막 도착 추가
    temp = list(map(int, input().split()))

    # 번호를 인덱스로 해서 충전기 위치를 표시(1)
    for i in range(len(temp)):
        power[temp[i]] = 1

    print("#{} {}".format(tc+1, find(power)))