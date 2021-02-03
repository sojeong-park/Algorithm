# 큰 수의 법칙
# 주어진 배열의 주어진 숫자를 M번 더해 가장 큰 수 만드는 법칙, 단 동일인덱스에 해당하는 수가 연속 K번 초과해 더해질 수 없다.
# 6 + 6+ 6 + 5+ 6 + 6 + 6 + 5
# 배열의 크기 N, 숫자가 더해지는 횟수 M, 그리고 K가 주어질때 큰 수의 법칙에 따라 가장 큰 수를 출력하시오
# 입력예시
# 5 8 3
# 2 4 5 4 6

n, m, k = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()
firstNum = arr[n-1] # 가장 큰 수
secondNum = arr[n-2] # 그다음으로 큰 수
tmpM = m

# 풀이1
sum = 0
while True:
    for i in range(k):
        if tmpM == 0:
            break
        sum += firstNum
        tmpM -= 1
    if tmpM == 0:
        break
    sum += secondNum
    tmpM -= 1
print(sum)

# 풀이2
z = m // (k+1) * k
z += m % (k+1)

sumFirst = firstNum * z
sumSecond = secondNum * (m-z)
print(sumFirst + sumSecond)