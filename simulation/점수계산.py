# 0: 틀린문제, 1: 맞은문제. 문제가 연속해서 맞을경우 가산점 준다
# 연속으로 문제의 답이있는 경우 두번째 문제는 2점, K번째 문제는 k점..

n = int(input())
grades = list(map(int, input().split()))

cnt = 1
sum = 0
for i in range(n):
    if grades[i] == 1:
        sum += cnt
        cnt += 1
    else:
        cnt = 1
print(sum)