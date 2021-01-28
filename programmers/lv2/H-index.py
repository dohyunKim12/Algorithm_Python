
def solution(citations):
    l = citations
    length = len(l)
    j = 0
    while True:
        cnt = 0
        for i in l:
            if i >= j:
                cnt += 1

        if j == cnt :
            ans = j
            break
        j += 1

    return ans


print(solution([3, 0, 6, 1, 5]))
