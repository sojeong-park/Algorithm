# https://www.acmicpc.net/problem/1141

n = int(input())
alpa_list = []
for _ in range(n):
    alpa_list.append(input())

def solution(alpa_list):
    alpa_list.sort(key=len)
    is_prefix = False
    cnt = 0
    for i in range(len(alpa_list)):
        for j in range(i+1, len(alpa_list)):
            if alpa_list[j].startswith(alpa_list[i]):
                is_prefix = True
                break
        if not is_prefix:
            cnt += 1
        is_prefix = False
    return cnt

print(solution(alpa_list))