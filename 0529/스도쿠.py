import sys
sys.stdin = open('ALGO1')

def check(x, y, num):
    # 가로줄 검사
    for i in range(9):
        if base[x][i] == num:
            return False
    # 세로줄 검사
    for j in range(9):
        if base[j][y] == num:
            return False

    # 3*3 칸 검사는 전체의 base를 각각의 3*3 를 따로 떼어 보았을 때 인덱스가 3을 기준으로 나뉘므로,
    # 각각의 좌표(x,y)를 3으로 나눈 몫을 다시 3으로 곱해주면 각각 3*3 칸의 0,0(맨 처음) 위치로 할당이 되고,
    #(새로 할당된 값이 각각 nx, ny)
    # 여기서 부터 각각의 가로 세로를 3칸씩 검사해주면(2중 for문) 같은 숫자가 있는지 없는지 확인 할 수 있다.
    nx = x // 3 * 3 # x를 새로 할당한 nx
    ny = y // 3 * 3 # y를 새로 할당한 ny
    # 각각의 3*3 칸에서...
    for a in range(nx, nx+3): #가로 3칸 검사
        for b in range(ny, ny+3): #세로 3칸 검사
            if base[a][b] == num:
                return False
    return True # 위 조건을 모두 만족하지 않으면, 해당 위치에 해당 숫자(x, y, num)를 base에 넣을 수 있다.

T = int(input())
for test_case in range(1, T+1):
    inp_num = int(input())
    base = [] # 스도쿠 베이스 판
    numbers = [] # 넣을 숫자들의 위치와 숫자가 담기는 이중배열리스트

    # 스도쿠 베이스 값 넣기(base 리스트에)
    for i in range(9):
        line = list(map(int, input().split()))
        base.append(line)

    # base리스트에 넣을 위치와 숫자 input값을 numbers 리스트에 모두 넣기(map으로 받게 되면, 뒤에 있는 인풋값이 없어지지 않아, 오류가 발생한다)
    cnt = 0
    for j in range(inp_num):
        number = list(map(int, input().split()))
        numbers.append(number)

    for a in range(len(numbers)): # 이중 배열 numbers를 풀면 각각의 number정보가 나온다
        # check함수를 통해 같은 값이 없는 지 체크하고, base에 넣기
        if check(numbers[a][0], numbers[a][1], numbers[a][2]) == True:
            if base[numbers[a][0]][numbers[a][1]] == 0: # 넣으려는 위치에 이미 값이 없는 지 확인한 후
                base[numbers[a][0]][numbers[a][1]] = numbers[a][2] # 값 넣기
                cnt += 1 # cnt 증가
        else: # 만약 같은 값이 있다면(check함수가 False라면)
            break # 멈춘다(해당 for문 탈출)

    print('#{} {}'.format(test_case, cnt))