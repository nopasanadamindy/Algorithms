#
# inch = float(input())
# cm = 2.54 * inch
# print('{} inch =>  {} cm'.format(inch, cm))

#13
# x = int(input())
#
# for i in range(1, x + 1):
#     if x % i == 0:
#         print('{}(은)는 {}의 약수입니다.'.format(i, x))

#14
# x = int(input())
#
# cnt = 0
# for i in range(1, x + 1):
#     if x % i == 0:
#         cnt += 1
#         print('{}(은)는 {}의 약수입니다.'.format(i, x))
# if cnt == 2:
#     print('{}(은)는 1과 {}로만 나눌 수 있는 소수입니다.'.format(x, x))

#15
# x = str(input())
#
# if x.islower():
#     print('{} 는 소문자 입니다.'.format(x))

#16
# Man1 = str(input())
# Man2 = str(input())
#
# if Man1 == '가위' and Man2 == '보':
#     print('Result : Man1 Win!')
#
# elif Man1 == '바위' and Man2 == '가위':
#     print('Result : Man1 Win!')
#
# elif Man1 == '보' and Man2 == '바위':
#     print('Result : Man1 Win!')
#
# elif Man1 == Man2:
#     print('Result : Draw')

#17.


#18
# result = []
# for x in range(1, 201):
#     if x % 7 == 0:
#         if x % 5 != 0:
#             result.append(x)
# for i in range(len(result) - 1):
#     print(result[i], end = ',')
# print(result[-1])



#19

# i = int(input())

# 1)
while 100 <= i <= 300:
    while i != 0 :
        if (i % 10) % 2 == 0:
            i = (i // 10)
            if (i % 2) == 0:
                print(i, end = ',')
        else:
            break
# 2) for

# for i in range(100, 301):
#     num = str(i)
#     for j in range(len(num)): #j는 idx num
#         if int(num[j]) % 2 != 0:
#             break
#     else:
#         print(num, end = ' ')


# 3) 선생님

# result = []
# for i in range(100, 301):
#     num =str(i)
#     flag = True
#     for j in range(len(num)):
#         if int(num[j]) % 2 != 0:
#             flag = False
#     if flag:
#         result.append(i)
#
# for i in range(len(result) - 1):
#     print(result[i], end=',')
# print(result[-1])