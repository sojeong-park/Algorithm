# 1로 만들기
# 주어진 정수 x를 4가지 연산을 이용해 1로 만들수 있는 최소 연산 회수는?
# 1. x가 5로 나누어 떨어지면 5로 나눈다.
# 2. x가 3로 나누어 떨어지면 3로 나눈다.
# 3. x가 2로 나누어 떨어지면 2로 나눈다.
# 4. x에서 1을 뺀다.

x = int(input())

d = [0] * (x+1)

for i in range(2, x+1):
    d[i] = d[i-1]+1
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2]+1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3]+1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i//5]+1)
print(d[x])