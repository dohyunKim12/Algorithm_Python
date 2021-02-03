def solution(arr):
    ans = []
    tmp = -1
    for i in arr:
        if i != tmp:
            ans.append(i)
        tmp = i
    return ans



print(solution([1,1,3,3,0,1,1]))
print(solution([4,4,4,3,3]))

