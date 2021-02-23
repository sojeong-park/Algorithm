# 0~9 정수로 이루어진 문자열 s가 주어졌을때, 곱하기 더하기 연산만으로 가장 큰 수를 구해라
# 입력예시1) 02984  출력예시1) 576
# 입력예시2) 567    출력예시2) 210
# 핵심 생각: 0과 1인 경우 곱하는 것보다 더하는 값이 더 크다 예)1+2=3, 1x2=2

arr = list(input())
result = int(arr[0])

for i in range(1, len(arr)):
    num = int(arr[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num
print(result)
