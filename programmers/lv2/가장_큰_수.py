numbers = []
numbers = list(map(int,input().split()))

def solution(numbers):
    numbers = list(map(str, numbers))
    length = len(numbers)

    stack = []
    while True:
        max_elem = numbers[0]
        for e in numbers:
            if e[0] > max_elem[0]:
                max_elem = e
            elif e[0] == max_elem[0]:
                if len(e) > len(max_elem) and e[-1] != '0':
                    max_elem = e
                elif len(e) == len(max_elem):
                    for i in range(len(max_elem)):
                        if e[i-1] > max_elem[i-1]:
                            max_elem = e

        stack.append(max_elem)
        del numbers[numbers.index(max_elem)]

        if len(stack) == length:
            break

    print(stack)

    return stack


ans = solution(numbers)
print(ans)
