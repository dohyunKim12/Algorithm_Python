arr =  list(map(int,(input().split())))

print(arr)

divisor = int(input())

print(divisor)

def solution(arr, divisor):
    answer = []

    for i in arr:
        if i % divisor == 0:
            answer.append(i)

    answer.sort()
    if len(answer)==0:
        answer.append(-1)
    return answer

answer = []
answer = solution(arr, divisor)

print(answer)
