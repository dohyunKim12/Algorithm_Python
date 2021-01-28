numbers = []
numbers = list(map(int,input().split()))

def solution(numbers):
    stack = []
    tmp = []
    length = len(numbers)

    numbers=  list(map(str, numbers))

    for index, number in enumerate(numbers):
        tmp.append((number * 4)[:4])

    tmp = list(map(int,tmp))

    while True:
        max_ = tmp[0]
        for e in tmp:
            if e > max_:
                max_ = e

        pop_i = tmp.index(max_)
        stack.append(numbers[pop_i])
        del numbers[pop_i]
        del tmp[pop_i]

        if len(stack) == length: break

    stack = ''.join(stack)
    return str(0) if not int(stack) else stack


ans = solution(numbers)
print(ans)


