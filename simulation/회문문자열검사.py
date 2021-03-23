# 회문문자열검사
# 회문 문자열일 경우 True, 아닐경우 False 출력

n = int(input())

for i in range(n):
    alpa = input().upper()
    # 풀이1
    j = len(alpa)-1
    for k in range(len(alpa)//2):
        if alpa[k] == alpa[j]:
            j -= 1
        else:
            print("NO")
            break
    else:
        print("Yes")

    #풀이2. 풀이 1번보다 간결함
    for k in range(len(alpa)//2):
        if alpa[k] != alpa[-1-k]:
            print("NO")
            break
    else:
        print("YES")

    #풀이3
    if alpa == alpa[::-1]:
        print("YES")
    else:
        print("NO")