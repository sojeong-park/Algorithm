# 뒤집은 소수
# N개의 자연수가 입력되면 각 자연수를 뒤집고 그 수가 소수이면 수를 출력하자.
# 첫자리부터 연속된 0은 무시한다.

n = int(input())
nums = list(map(int, input().split()))
prime = [0] * 100001

def reverse(x):
    ans = 0
    while x > 0:
        num = x % 10
        ans = ans * 10 + num
        x //=10
    return ans


def isPrime(x):
    if x == 1:
        return False
    for i in range(2, x//2+1):
        if x % i == 0:
            return False
    else:
        return True

reverseNums = []
for i in nums:
    reverseNums.append(reverse(i))

maxReverseNum = max(reverseNums)


# 소수 판별
for i in range(2, maxReverseNum+1):
    if prime[i] == 0:
        for j in range(i, maxReverseNum+1, i):
            prime[j] += 1

for i in reverseNums:
    if isPrime(i):
        print(i, end=" ")
