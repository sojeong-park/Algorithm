# 팀결성 - 298p
# 문제 규칙
#   같은팀 여부확인:1, 팀 합치기:0 ex) 0 1 3 -> 1번과 3번 학생 팀결성, 1 1 7 -> 1번과 7번 학생 같은팀인지 판별
# 입력 예시
# 7 8
# 0 1 3
# 1 1 7
# 0 7 6
# 1 7 1
# 0 3 7
# 0 4 2
# 0 1 1
# 1 1 1

def findParent(parent, x):
    if parent[x] != x:
        parent[x] = findParent(parent, parent[x])
    return parent[x]

def unionParent(parent, a, b):
    a = findParent(parent, a)
    b = findParent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n,m = map(int, input().split())

parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i

for i in range(m):
    flag, a, b = map(int, input().split())
    if flag == 0: # 팀 합치기
        unionParent(parent, a, b)
    else:
        if findParent(parent,a) != findParent(parent, b):
            print('NO')
        else:
            print('YES')