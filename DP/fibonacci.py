# 피보나치 구현 - 1. 재귀 2. 반복문

# 1. 재귀함수 구현 :식 Top-Down 방식, memoization 구현
d = [0] * 100
def fibo(n):
    if n == 1 or n == 2:
        return 1
    if d[n] != 0: #이미 계산한적이 있는 함수
        return d[n]
    d[n] = fibo(n-1) + fibo(n-2)
    return d[n]

# 2. 반복문 : Bottom-up 방식
n = 99
k = [0] * 100
k[1] = 1
k[2] = 1
for i in range(3, n+1):
    k[i] = k[i-1] + k[i-2]

print(k[n])