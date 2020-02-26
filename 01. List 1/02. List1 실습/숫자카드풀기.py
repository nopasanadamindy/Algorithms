import sys
sys.stdin = open('숫자카드.txt')

T = int(input())
for test_case in range(1, T + 1):
    length = int(input())
    num = list(map(int, input()))

    cnt = [0 for i in range(10)]
    max_cnt = 0
    max_idx = 0
    #1. 반복문을 사용해서 num 추출하기 -> 해당 숫자를 idx로 할당
    for i in num:
        cnt[i] += 1
    # print(cnt)
    #2. cnt 중 가장 큰 값 max_cnt로 추출
    for j in range(len(cnt)):
        if cnt[j] >= max_cnt:
            max_cnt = cnt[j]
            max_idx = j

    #3. 만약 max_cnt가 같을 경우 idx넘버가 큰 값 추출
        if max_cnt == cnt[j]:
            if j >= max_idx:
                max_idx = j
    print(max_idx)

    print('#{} {} {}'.format(test_case, max_idx, max_cnt))