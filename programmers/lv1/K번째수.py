array = list(map(int, input("array입력: ").split()))

commands = []
length = int(input("commands의 길이 입력: "))
for i in range(length):
    commands.append([])
    print(i, end='')
    commands[i] = list(map(int,input("번째 줄 입력: ").split()))

print(commands)


def solution(array, commands):
    ans = []
    length= len(commands)

    for i in range(length):
        new_array = []
        start_index = commands[i][0]
        end_index = commands[i][1]
        extract_index = commands[i][2]
        new_array = array[start_index-1:end_index]
        new_array.sort()
        ans.append(new_array[extract_index-1])
    return ans

ans = []
ans = solution(array, commands)
print(ans)
