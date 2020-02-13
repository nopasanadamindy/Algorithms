import sys
sys.stdin = open('색칠하기.txt')


T = int(input())
for test_case in range(1, T + 1):

    length = int(input())
    result = [[0 for i in range(10)] for i in range(10)]

    for _ in range(length):
        c1, r1, c2, r2, color = map(int, input().split())

        if color == 1:
            for i in range(r1, r2 + 1):
                for j in range(c1, c2 + 1):
                    result[i][j] += 1

        if color == 2:
            for i in range(r1, r2 + 1):
                for j in range(c1, c2 + 1):
                    result[i][j] += 2

    cnt = 0
    for _ in range(r1, r2 + 1):
        for _ in range(c1, c2 + 1):
            if result[i][j] == 3:
                cnt += 1

    print('#{} {}'.format(test_case, cnt))




T = int(input())

for test_case in range(1, T + 1):

    length = int(input())
    result = [[0 for _ in range(10)] for _ in range(10)]

    for i in range(length):
        c1, r1, c2, r2, color = map(int, input().split())

        if color == 1:
            for i in range(r1, r2 + 1):
                for j in range(c1, c2 + 1):
                    result[i][j] += 1

        if color == 2:
            for i in range(r1, r2 + 1):
                for j in range(c1, c2 + 1):
                    result[i][j] += 2

    cnt = 0
    for i in range(len(result)):
        for j in range(len(result)):
            if result[i][j] == 3:
                cnt += 1

    print('#{} {}'.format(test_case, cnt))


