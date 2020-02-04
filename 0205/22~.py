#22
# for i in range(1, 101):
#     print(i)

#23
# for i in range(1, 101):
#     if i % 2 == 0:
#         print(i, end = ' ')

#24
# result = []
# for i in range(1, 100, 2):
#     result.append(i)
#
# for i in range(len(result) - 1):
#     print(result[i], end = ', ')
# print(result[-1])

#25
# result = 0
#
# for i in range(1, 101):
#     if i % 3 == 0:
#         result += i
# print('1부터 100사이의 숫자 중 3의 배수의 총합: {}'.format(result))

# #26
# blood_type = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
# new = {}
# for blood in blood_type:
#     if blood not in new:
#         new[blood] = 1
#     else:
#         new[blood] += 1
# print(new)

# 27
# score = [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]

#1) while, pop
# high = []
# for i in range(len(score)):
#     while 80 <= score[i]:
#         high.append(score[i])
#         i += 1
# print(high)

#1-2)
# for i in range(len(score)):
#     while score[i] <= 80:
#         score.pop(i)
# print(score)

#2) for
# new = []
# for i in range(len(score)):
#     if score[i] >= 80:
#         new.append(score[i])
# result = 0
# for i in new:
#     result += i
# print(result)

# #3) sorted
# s_score = sorted(score)
# # print(s_score)
# for i in range(len(score)):
#     if s_score[i] >= 80:
#         # print(i)
#         break
#         s_sort.pop(i::)
# print(s_score)

#28
# i = 5
# while i >= 1:
#     star = ('*' * i)
#     print(star)
#     i -= 1

#29

#30
# num = int(input())
# norm = list(range(10))
# result = [0 for i in range(5)]

# number = str(num)
# for i in len(number):
#     i = int(number)[i] 
#     result. append([i])

# for i in norm:
#     print(i, end = ' ')
# if 


#31.
