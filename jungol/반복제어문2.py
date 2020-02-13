# 541
# inp = input()
# a = inp * 20
# print("{}" .format(a))


# # 542
# for i in range(10, 20 + 1):
#     print(i)

# 543
#1) for문
# inp = int(input())
# for i in range(1, inp + 1):
#     if i % 2  == 0:
#         print(i, end = ' ')

#2) while : 초기식/조건식/증감식
# inp = int(input())
# i = 1
# while i <= inp:
#     if i % 2 == 0:
#         print(i, end = ' ')
#     i += 1

# 544.
#1) while : 초기식/조건식/증감식
# inp = int(input())
# sum = 0
# while inp <= 100:
#     sum += inp
#     inp += 1
# print(sum)
#
# #2) for
# inp = int(input())
# sum = 0
# for i in range(inp, 101):
#     sum += i
# print(sum)

# 545
# num = list(map(int, input().split()))
#
# # 1) for
# cnt_3 = 0
# cnt_5 = 0
# for i in range(len(num)):
#     if num[i] % 3 == 0:
#         cnt_3 += 1
#     if num[i] % 5 == 0:
#         cnt_5 += 1
# print('Multiples of 3 : {}'.format(cnt_3))
# print('Multiples of 5 : {}'.format(cnt_5))
# # 10 15 36 99 100 19 46 88 87 13

# 2) while : 초기/조건/증감식
# num = list(map(int, input().split()))
# i = 0
# cnt_3 = 0
# cnt_5 = 0
# while i <= len(num) - 1:
#     if num[i] % 3 == 0:
#         cnt_3 += 1
#     if num[i] % 5 == 0:
#         cnt_5 += 1
#     i += 1
# print('Multiples of 3 : {}'.format(cnt_3))
# print('Multiples of 5 : {}'.format(cnt_5))

# 546.
# 4
# 75 80 85 90

# N = int(input())
# score = list(map(int, input().split()))

# 1) for
# sum = 0
# for i in score:
#     sum += i
# if (sum/N) >= 80:
#     print('avg : {}'.format(round(sum/N, 1)))
#     print('pass')
# else:
#     print('avg : {}'.format(round(sum/N, 1)))
#     print('fail')

#2) while 초기값/조건식/증감식
# N = int(input())
# score = list(map(int, input().split()))
#
# i = 0
# sum = 0
# while i < N:
#     sum += score[i]
#     i += 1
#
# if (sum/N) >= 80:
#     print('avg : {}'.format(round(sum / N, 1)))
#     print('pass')
# else:
#     print('avg : {}'.format(round(sum / N, 1)))
#     print('fail')

# # 547. X
#
# for i in range(6):
#     for j in range(6):
#         print(i, j)
# arr = [[0 for i in range(6)] for i in range(6)]
# print(arr)

## 548. O
# for i in range(2, 10):
#     for j in range(1, 10):
#         print('{} * {} =  {}   '.format(i, j, i*j))

## 130
# 1) for
# word = 'JUNGOL'
# inp = int(input())
# for i in range(inp):
#     print(word)

# 2) while 초기/조건/종료
# inp = int(input())
# i = 0
# word = 'JUNGOL'
# while i < inp:
#     print(word)
#     i += 1

# 131
# 100 이하의 두 개의 정수를 입력받아 작은 수부터 큰 수까지 차례대로 출력하는 프로그램을 작성하시오.
# 입력 예) 10 5
# 출력 예) 5 6 7 8 9 10

# inp = list(map(int, input().split()))
# m = max(inp)
# mi = min(inp)
# for i in range(mi, m + 1):
#     print(i, end = ' ')

#132
# 1) while
# num = int(input())
# i = min(num)
# sum = 0
# while i <= max(num):
#     if i % 5 == 0:
#         sum += i
#     i += 1
# print(sum)

#2) for
# num = int(input())
# sum = 0
# for i in range(num + 1):
#     if i % 5 == 0:
#         sum += i
# print(sum)

## 133.
# N = int(input())
# num = list(map(int, input().split()))
#
# sum = 0
# for i in num:
#     sum += i
# print(round(sum/N, 2))

#2) while
# N = int(input())
# num = list(map(int, input().split()))
# i = 0
# sum = 0
# while i < len(num):
#     sum += num[i]
#     i += 1
# print(round(sum/N, 2))


## 134.
# 1) for문
# num = list(map(int, input().split()))
#
# cnt_even = 0
# cnt_odd = 0
# for i in num:
#     if i % 2 == 0:
#         cnt_even += 1
#     else:
#         cnt_odd += 1
# print('even : {}'.format(cnt_even))
# print('odd : {}'.format(cnt_odd))

# 2) While문
# num = list(map(int, input().split()))
# cnt_even = 0
# cnt_odd = 0
# i = 0
# while i < len(num):
#     if num[i] % 2 == 0:
#         cnt_even += 1
#     else:
#         cnt_odd += 1
#     i += 1
# print('even : {}'.format(cnt_even))
# print('odd : {}'.format(cnt_odd))

## 135.
# a, b = map(int, input().split())
# s = 0
# e = 0
# if a > b:
#     s = b
#     e = a
# else:
#     s = a
#     e = b
#
# sum = 0
# cnt = 0
# for i in range(s, e + 1):
#     if i % 3 == 0 or i % 5 == 0:
#         sum += i
#         cnt += 1
#
# print('sum : {}'.format(sum))
# print('avg : {}'.format(round(sum/cnt, 1)))

## 136
arr = [[0 for i in range(4)] for i in range(3)]

# for i in range(1, 3 + 1):
#     for j in range(1, 4 + 1):
#         arr[i-1][j-1] = i * j
#         # print(arr[i][j], end = ' ')
#     print(arr[i-1])
#
# a, b = map(int, input().split())
# for i in range(1, a + 1):
#     for j in range(1, b + 1):
#         arr[i-1][j-1] = i * j
#         print(arr[i-1][j-1], end = ' ')
#     print()

arr = [[0 for i in range(4)] for i in range(3)]

a, b = map(int, input().split())
for i in range(1, a + 1):
    for j in range(1, b + 1):
        arr[i-1][j-1] = i * j
        print(arr[i-1][j-1], end = ' ')
    print()



#
# 137.
# a, b = map(int, input().split())
#
# for i in range(1, a + 1):
#     for j in range(1, b + 1):
#         print(i * j, end = ' ')
#     print()

# 137.
# a, b = map(int, input().split())
# arr = [[0 for _ in range(b)] for _ in range(a)]
# # print(arr)
# for i in range(a):
#     for j in range(b):
#         arr[i][j] = (i+1) * (j+1)
#     print(arr[i])