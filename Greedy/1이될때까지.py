# N의 값이 1이 될때까지 다음위 두과정 중 하나를 반복적으로 선택하여 수행한다.
# 1. N에서 1을 뺀다
# 2. N을 K로 나눈다. -> N이 K로 나우어 떨어질때만 가능
# 1로만드는 연산의 최소횟수는?

n, k = map(int, input().split())
tmpN = n

count = 0
while True:
    if n == 1:
        break
    if n % k != 0:
        n -= 1
        count += 1
    else:
        n //= k
        count += 1
print(count)

# 방법2
result = 0
while True:
    target = (tmpN // k) * k    # k와 가장 근접한 배수 생성
    result += (tmpN-target)     # 빼기 연산횟수 더하기
    tmpN = target               # n에 배수값 입력
    if tmpN < k:                # n의 값이 k보다 작다면 나눌수 없으니 빠져나오기
        break
    result += 1                 # 나누기 연산횟수 더하기
    tmpN //= k                  # k의 값으로 나누기
result += (tmpN-1)              # 1로 만들기 위해 숫자 빼기
print(result)