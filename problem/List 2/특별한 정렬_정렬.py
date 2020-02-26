# def bubble(a):
#     for i in range(len(a)-1, 0, -1):
#         for j in range(0, i):
#             if a[j] > a[j+1]:
#                 a[j], a[j+1] = a[j+1], a[j]

def sorting(a):
    for i in range(0, len(a)-1):
        min = i
        for j in range(i+1, len(a)):
            if a[min] > a[j]:
                a[min], a[j] = a[j], a[min]
import sys
sys.stdin = open('특별한 정렬.txt')

T = int(input())
for test_case in range(1, T+1):
    length = int(input())
    data = list(map(int, input().split()))
    # print(data)
    sorting(data)

    result = []
    for x in range(len(data)-1):
        result.append(data[len(data)-1 - x])
        result.append(data[x])
    print(result)

    # print('#{}'.format(test_case), end = ' ')
    # for i in range(10):
    #     print(result[i], end = ' ')
    # print()
    # maxi = len(data) - 1
    # mini = 0
    # cnt = 0
    # while cnt < 5:
    #     result.append(data[maxi])
    #     result.append(data[mini])
    #     maxi -= 1
    #     mini += 1
    #     cnt += 1
    # print('#{}'.format(test_case), end = ' ')
    # for i in range(len(result)):
    #     print(result[i], end = ' ')
    # print()