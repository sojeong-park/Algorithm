# n = 배열의 크기, k = 원소 교체 가능 횟수
# A,B의 배열이 주어지면 A와 B의 원소를 교환해 A의 모든 원소의 합이 최댓값이 되도록 하자.

n, k = map(int, input().split())

# 방법1
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))

for i in range(k):
    minNum = a[i]
    maxNum = b[n-i-1]
    a[i], b[n-i-1] = maxNum, minNum

print(sum(a))

#방법2
c = list(map(int, input().split()))
d = list(map(int, input().split()))

c.sort()
d.sort(reverse=True)

for i in range(k):
    if c[i] < d[i]:
        c[i], d[i] = d[i], c[i]
    else:
        break
print(sum(c))