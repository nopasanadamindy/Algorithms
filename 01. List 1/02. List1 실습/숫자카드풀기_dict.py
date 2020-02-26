import sys
sys.stdin = open('숫자카드.txt')
# 가장 많은 카드의 숫자와 장수를 차례때로 출력한다.
T = int(input())
for test_case in range(1, T + 1):
    length = int(input())
    num = list(map(int, input()))
    result = {}

    #1. 딕셔너리에 추가해서 카운팅하기
    for i in num:
        if i not in result:
            result[i] = 1
        else:
            result[i] += 1
    #2.items를 활용하여 key, val도출
    # max_cnt = 0
    # max_card = 0
    # for card_num, card_cnt in result.items():
    #     if card_cnt >= max_cnt:
    #         max_cnt = card_cnt
    #         if max_card < card_num:
    #             max_card = card_num
    # print('#{} {} {}'.format(test_case, max_card, max_cnt))


    #2.items를 활용하여 key, val도출
    # max_cnt = 0
    # max_card = 0
    # for card_num, card_cnt in result.items():
    #     if card_cnt >= max_cnt:
    #         max_cnt = card_cnt
    #         max_card = card_num
    # print(max_card, max_cnt)