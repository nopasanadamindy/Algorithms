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
# 다음은 학생의 점수를 나타내는 리스트입니다.
# [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
# while 문과 리스트 객체의 pop()을 이용해 80점 이상의 점수들의 총합을 구하시오.
#     답 _ 454
#
# score = [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
#
# summation = 0
# while bool(score):
#     s = score.pop()
#     if s >= 80:
#         summation += s
# print(summation)

# while score[i] >= 80:
#     for i in range(len(score)):
#         h_score = score.pop(i)
#         summation += h_score
# print(summation)


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

# 2) for
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
#
# i = 7
# j = 0
# while i >= 1:
#     star = (' ' * j)+ ('*' * i)
#     print(star)
#     i -= 2
#     j += 1
#
# i = 7
# j = 0
# while i >= 1:
#     star = (' ' * j) + ('*' * i)
#     print(star)


#30
#
# def conv(a):
#     return list(a)
#
# # num = int(input())
# num = 123
#
# #1)) 빈 딕셔너리 만들어주기
# dict = {}
#
# #2)) key값과 val값 추가하기
# for i in range(10):
#     dict[i] = 0
#
# #3)) num를 스트링으로 하나씩 잘라서 카운트 해주기
# number = str(num)
# for i in number:
#     dict[int(i)] += 1
#
# #4) 추출
#
# for i in dict.keys():
#     a = conv(str(i))
# for i in dict.values():
#     b = conv(str(i))
#
# print(a)
# print(b)


# #추가
# num = 55
# idx = list(range(10))
# cnt = [0 for i in range(10)]

#1)) num -> str
# number = str(num)
#2)) 하나씩 꺼내서 그 숫자를 idx num로 저장
# for i in number: # 효과적인 방법이 있을까?
#     ii = int(i)
#     cnt[ii] += 1
#
#3)) 출력 포맷
# result_i = ''
# result_c = ''
# for i in idx:
#     result_i += str(i) + ' '
#
# for i in cnt:
#     result_c += str(i) + ' '
#
# print(result_i)
# print(result_c)

