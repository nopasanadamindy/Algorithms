
## 03
# a = (90, 80)
# b = (85, 75)
# c = (90, 100)
#
# def summation(a):
#     return sum(a)
#
# def aver(a):
#     return average(a)

# print('{}번 학생의 총점은 {}점이고, 평균은 {}입니다.'.format(, summation())


## 04

# sentence = 'Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.'
#
# delete = 'aeiou'

# result = [i for i in sentence if i not in delete]
# print(''.join(result))

# for i in sentence:
#     for j in delete:
#         if i == j:
#             sentence.remove(i)
# print(sentence)


# numbers = [1, 2, 1, 3, 4, 1]
#
# target_value = 1
#
# for i in range(numbers.count(target_value)):
#     numbers.remove(target_value)
#
# print(numbers)

## 05.

# gugu = [i * j for i in range(2, 10) for j in range(1, 10)]
# # print(gugu)
#
# for x in gugu:
#     if x % 3 == 0 or x % 7 == 0:
#         dele = gugu.pop(x)
# print(dele)


## 06.

# result = []
# inp = int(input())
#
# print(result.append(inp))


## 07.

# inp = int(input())
# result = []
#
# for i in range(1, inp + 1):
#     if inp % i == 0:
#         result.append(i)
#
# print(result)

## 08.

# inp = int(input())
# result = []
#
# for i in range(1, inp + 1):
#     if inp % i == 0:
#         result.append(i)
#
# print(result)

## 09.

# ex = [1, 3, 11, 15, 23, 28, 37, 52, 85, 100]
#
# result = [i for i in ex if i % 2 == 0]
# print(result)


## 11.

# def cubic(a):
#     return a**2
# triple = []
# for i in range(1, 20 +1):
#     if i % 3 != 0 or i % 5 != 0:
#         result = cubic(i)
#         triple.append(result)
# print(triple)
#
# triple = [i ** 2 for i in range(1, 20 + 1) if i % 3 != 0 or i % 5 != 0]
# print(triple)

## 12.

# number = 12345
#
# s_num = str(number)
# result = 0
#
# for i in range(len(s_num)):
#     result += int(s_num[i])
#
# print(result)



###2)
# number = 12345
# result = 0
#
# while number % 10 != 0:
#     result += (number % 10)
#     number = (number // 10)
# print(result)



## 14.

# inp = list(map(int, input().split(', '))
# inp2 = set(inp)


# 15.

# 1)
# inp = list(map(int, input().split(', ')))
#
# def cir(a):
#     return a * 3.14 * 2
#
# for i in inp:
#     print(cir(i), end = ', ')
#
# # 2)
#
# inp = list(map(int, input().split(', ')))
#
# for i in inp:
#     print('{.2f}'.format(i * 3.14 * 2, end = ', '))


# 17.

# word = list(map(str, input().split(', ')))
# result = ''
# result += sorted(word)
# print(result)

#
# word = python, hello, world, hi
# result = list(map(str, word.split(', ')))
#
# print(result)



# 19.

# inp = (1,2,3,4,5,6,7,8,9,10)
#
# def half(a):
#     for i in range(len(a)):
#
#
# for i in range(len(inp)):

## 20.

number = [5, 6, 77, 45, 22, 12, 24]
s = str(number)
for i in range(len(s)):
    if int(s[i]) % 2 == 0:
        even = list(number.pop(i))