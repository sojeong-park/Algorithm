# 2020 카카오 신입 공채
# https://programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    newStr = ""
    answer = len(s)
    for i in range(1, len(s)//2+1):
        j = 0
        count = 1
        while j < len(s):
            a = s[j : j+i]
            b = s[j+i : j+(i*2)]
            if a == b:
                count += 1
                j += i
            else:
                if count > 1:
                    newStr += str(count)
                    newStr += a
                    count = 1
                else:
                    newStr += a
                j += i
        if answer > len(newStr):
            answer = len(newStr)
        newStr=""

    return answer


s1 = "a"
s2 = "abced"
s3 = "abcabcdede"
print(solution(s1))
