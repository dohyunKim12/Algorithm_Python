def solution(s):
    center_i = len(s)/2
    if center_i % 1 == 0:
        cent = int(center_i)
        ans = s[cent-1:cent+1]
    else:
        ans = s[int(center_i)]
    return ans


print(solution('abcde'))
print(solution('qwer'))
