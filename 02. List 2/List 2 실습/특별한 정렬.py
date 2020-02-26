import sys
sys.stdin = open("특별한정렬_input.txt")

T = int(input())
for test_case in range(1, T + 1):
    crr = []
    a = int(input())
    b = list(map(int,input().split()))
    for i in range(len(b)):
        for j in range(len(b)-1):
            if b[j]<b[j+1]:
                b[j],b[j+1] = b[j+1],b[j]
    print('#{} '.format(test_case),end ='')
    for i in range(5):
        if i ==4:
            print('{} {}'.format(b[0+i],b[a-1-i]))
        else:
        	print('{} {}'.format(b[0+i],b[a-1-i]),end =' ')