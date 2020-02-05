
blood_type = {'A': 4, 'B': 2, 'AB': 3, 'O':1}

# result = '혈액형의 종류는 다음과 같습니다 => '
# for blood in blood_type:
#     result += blood + ' '
# print(result)


for blood in blood_type.keys():
    print('혈액형의 종류는 다음과 같습니다 => {}'.format(blood))

