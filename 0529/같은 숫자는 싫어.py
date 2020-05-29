arr = [1,1,3,3,0,1,1]
def solution(arr):
    answer = []
    bin = []
    for i in range(1, len(arr)):
        if len(answer) == 0:
            answer.append(arr[i-1])
            # print(i)
        else:
            if answer[i-2] != arr[i-1]:
                answer.append(arr[i-1])
            else:
                bin.append(arr[i-1])
    print(answer)

solution(arr)