
def solution(citations):
    ans = 0
    j = 0
    for k in range(max(citations)):
        cnt = 0
        for i in citations:
            if i >= j:
                cnt += 1

        if j == cnt :
            ans = j
            break
        elif j <= cnt:
            ans = j
        j += 1

    return ans

print(solution([10,9,4,1,1]))
print(solution([0,1,3,5,5,5,5,5,5,6]))
print(solution([0,1,1,1,1,3,3,4]))
print(solution([0,0,0,0]))
