def bubble(data):
    for i in range(len(data)-1, 0, -1):
        for j in range(0, i):
            if data[j] < data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]

import sys
sys.stdin = open('(1206)View_input.txt')

T = 10
for test_case in range(1, 1 + T):
    length = int(input())
    data = list(map(int, input().split()))
    cnt = 0
    for i in range(2, length - 2):
        slicing = data[i-2:i+3]
        bubble(slicing)
        if data[i] == slicing[0]:
            cnt = cnt + (slicing[0] - slicing[1])
    print('#{} {}'.format(test_case, cnt))

# T = 10
# for test_case in range(1, 1 + T):
#     length = int(input())
#     data = list(map(int, input().split()))
#     cnt = 0
#     for i in range(2, length - 2):
#         slicing = sorted(data[i-2:i+3])[::-1]
#         if data[i] == slicing[0]:
#             cnt = cnt + (slicing[0] - slicing[1])
#     print('#{} {}'.format(test_case, cnt))