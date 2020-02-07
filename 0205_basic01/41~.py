## 41

## 1-1)
# def square(a):
#     return 'square({}) => {}'.format(a, a**2)
# print(square(2))
# print(square(3))
#
## 1-2) input값만 다르게 받음/근데 왜 런타임에러나????
# a, b = map(int, input().split())
#
# def square(a):
#     return 'square({}) => {}'.format(a, a**2)
#
# print(square(a))
# print(square(b))

## 42

# a, b = map(str, input().split(', '))
# def long(a, b):
#     if len(a) > len(b):
#         return a
#     else:
#         return b
#
# print(long(a, b))

# 43
def countdown(num):
    if num <= 0:
        print('카운트다운을 하려면 0보다 큰 입력이 필요합니다.')
    else:
        while num > 0:
            print(num)
            num -= 1
countdown(0)
countdown(10)

# def summation(a):
#     sum = 0
#     for i in range(a+1):
#         sum += i
#     print(sum)
#
# a = summation(100) + summation(10)
#
# summation(a)

#우리가 무슨 숫자를 받아서 0부터 그숫자까지 더할 건데 그 행위를 100번해야돼 그러면



#print(countdown(5))

## 47

# def isNum(a):
#     if type(a) == type(5):
#         s = str(a)
#         result = 1
#         for i in range(len(s)):
#             result *= s[i]
#         return result
#
#     else:
#         return '에러발생'
#
# a = 56
# print(isNum(a))

## 50


## 51 람다??


## 52
# num = (3, 5, 4, 1, 8, 10, 2)
# m = max(num)
# print('max{} => {}'.format(num, m))

## 53
# a = 'abcde'
# x = {}
# for i in range(len(a)):
#     x[a[i]] = i
# for idx, num in x.items():
#     print(idx, num)

