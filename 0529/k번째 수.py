array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command
        answer.append(sorted(array[i-1:j]))
    return answer

print(solution(array, commands))

# def solution(array, commands):
#     ans = []
#     for i in range(len(commands)):
#         criteria = []
#         for j in range(len(commands[i])):
#             criteria.append(commands[i][j])
#         arr  = array[criteria[0]-1:criteria[1]]
#         sorted_arr = sorted(arr)
#         ans.append(sorted_arr[criteria[2]-1])
#     return ans

