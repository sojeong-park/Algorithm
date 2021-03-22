# 각 자연수의 자릿수의 합을 구하고 그 합이 최대인 자연수를 출력해라
# 입력
# 3
# 123 15232 97
# 출력
# 97

n = int(input())
nums = input().split()
max = -1e9
def digit_sum(x):
    sum = 0
    for i in x:
        sum += int(i)
    return sum

for i in nums:
    total = digit_sum(i)
    if total > max:
        max = total
        res = i
print(res)