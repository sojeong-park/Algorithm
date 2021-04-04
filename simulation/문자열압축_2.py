# 문자열 압축 풀이 2
# https://programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    answer = len(s)
    for step in range(1, len(s)//2 + 1):
        compressed = "" # 압축문자열
        prev = s[0:step]
        count = 1
        for i in range(step, len(s), step):
            if prev == s[i: i+step]:
                count += 1
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[i: i+step]
                count = 1
        compressed += str(count) + prev if count >= 2 else prev
        answer = min(answer, len(compressed))
    return answer


s1 = "a"
s2 = "abced"
s3 = "abcabcdede"
print(solution(s3))
