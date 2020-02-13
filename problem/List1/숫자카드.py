import sys
sys.stdin = open("숫자카드.txt")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    num_list = list(map(int, input()))
    # print(num_list)

    max_num = num_list[0]
    max_cnt = 0
    for i in range(N):
        if num_list.count(i) >= max_cnt:
            max_cnt = num_list.count(i)
            max_num = i

    print('#{} {} {}'.format(test_case, max_num, max_cnt))