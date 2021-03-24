# 오름차순으로 정렬이 된 두리스트가 주어지면 두 리스트를 오름차순으로 합쳐 출력
# 입력
# 3
# 1 3 5
# 5
# 2 3 6 7 9

n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

p1, p2 = 0, 0
c = []
while p1 < n and p2 <m:
    if a[p1] < b[p2]:
        c.append(a[p1])
        p1 += 1
    else:
        c.append(b[p2])
        p2 += 1

if p1 == n:
    c += b[p2:m+1]
else:
    c += a[p1:n+1]

print(c)