
# 536. O
# i = 1
# while i <= 15:
#     print(i, end = ' ')
#     i += 1
#
# for i in range(1, 15 + 1):
#     print(i)

# 537. O
# num = int(input())
# i = 1
# sum = 0
# while i <= num:
#     sum += i
#     i += 1
# print(sum)

# 538 O
#
# while True:
#     inp = int(input('number? '))
#     if inp > 0:
#         print('positive integer')
#     elif inp < 0:
#         print('negative number')
#     else:
#         break
# 539 O
# 1)
# num = list(map(int, input().split))
# sum = 0
# cnt = 0
# i=0
# while True:
#     if num[i] < 100:
#         sum += num[i]
#         cnt += 1
#     else:
#         sum += num[i]
#         cnt += 1
#         break
#     i+=1
#
# print(sum)
# print(sum/cnt)
#
# # 2)
# num = list(map(int, input().split()))
# sum = 0
# cnt = 0
# for i in num:
#     if i < 100:
#         sum += i
#         cnt += 1
#     else:
#         sum += i
#         cnt += 1
#         break
# print(sum)
# print(round(sum/cnt, 1))

#1) while문
# num = list(map(int, input().split()))
# i = 0
# sum = 0
# cnt = 0
# while len(num):
#     if num[i] < 100:
#         sum += num[i]
#         cnt += 1
#         i += 1
#     else:
#         sum += num[i]
#         cnt += 1
#         break
#
# print(sum)
# print(round(sum/cnt, 1))

#2) for문
# num = list(map(int, input().split()))
# sum = 0
# cnt = 0
# for i in num:
#     if i <100:
#         sum += i
#         cnt += 1
#     else:
#         sum += i
#         cnt += 1
#         break
# print(sum)
# print(round(sum/cnt, 1))

# 540 O
# #1) While문
# while True:
#     num = int(input())
#     if num % 3 == 0:
#         print(num//3)
#     elif num == -1:
#         break
#     elif num % 3 != 0:
#         continue

# 633

# 125 O
# num = int(input())
# i = 1
# while i <= num:
#     print(i, end = ' ')
#     i += 1


# 126 O
#1) while문
# num = list(map(int, input().split()))
# i = 0
# odd_cnt = 0
# even_cnt = 0
# while True:
#     if num[i] == 0:
#         break
#     if num[i] % 2 == 0:
#         even_cnt += 1
#     else:
#         odd_cnt += 1
#     i += 1
# print('odd : {}'.format(odd_cnt))
# print('even : {}'.format(even_cnt))

# 127 O
# 1) while문
# num = list(map(int, input().split()))
# i = 0
# sum = 0
# cnt = 0
# while i < len(num):
#     if num[i] >= 0 and num[i] <= 100:
#         sum += num[i]
#         cnt += 1
#     else:
#         break
#     i += 1
# print('sum : {}'.format(sum))
# print('avg : {}'.format(round(sum/cnt, 1)))

# 2) for문
# num = list(map(int, input().split()))
# sum = 0
# cnt = 0
# for i in range(len(num)):
#     if num[i] >= 0 and num[i] <= 100:
#         sum += num[i]
#         cnt += 1
#     else:
#         print('sum : {}'.format(sum))
#         print('avg : {}'.format(round(sum / cnt, 1)))

# 128.
#1)
# num = list(map(int, input().split()))
# result = []
# i = 0
# while num[i] != 0:
#     result.append(num[i])
#     i += 1
# print(result)
#
# cnt = 0
# for number in result:
#     if (number % 3) != 0 and (number % 5) != 0:
#         # print(number)
#         cnt += 1
# print(cnt)

#2)
# num = list(map(int, input().split()))
# result = []
# i = 0
# while num[i] != 0:
#     if num[i] % 3 != 0 and num[i] % 5 != 0:
#         result.append(num[i])
#     i += 1
# print(len(result))

# 129.??
# while True:
#     base = int(input('Base = '))
#     height = int(input('Height = '))
#     print('Triangle width = {}'.format(base * height * 0.5))
#     inp = input('Continue? ')
#     if inp == 'Y' or inp == 'y':
#         continue
#     else:
#         break
