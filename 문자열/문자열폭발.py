# https://www.acmicpc.net/problem/9935

# 문자열 폭발 - 투포인터로 폭발할 문자열 찾고 합치기

n = input() # 주어진 문자열
x = input() # 폭발할 문자열

# 시간초과 발생
def solution(n, x):
    left = n.find(x)
    right = left + len(x)

    while left != -1 :
        n = n[:left] + n[right:]
        left = n.find(x)
        right = left + len(x)
    if len(n) == 0:
        return 'FRULA'
    return n

print(solution(n, x))

# 스택으로 구현
def stack_solution(n, x):
    s = []
    lastBomb = x[-1]
    x_len = len(x)
    for char in n:
        s.append(char)
        if char == lastBomb and ''.join(s[-x_len:]) == x:
            del s[-x_len:]
    ans = ''.join(s)
    if ans == '':
        return 'FRULA'
    return ans
print(stack_solution(n,x))