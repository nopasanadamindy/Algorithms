
import sys
sys.stdin = open("0208.txt")

T = int(input())
length = str(input())
num = input().split()
numbering = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

# 빈리스트에 넣을거야
result = []

for test_case in range(1, T + 1):
    for i in range(len(numbering)):
        for j in range(len(num)):
            if numbering[i] == num[j]:
                result.append(num[j])


    print('#{}'.format(test_case))
    print(' '.join(result))

