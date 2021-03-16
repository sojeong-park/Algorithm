# https://www.acmicpc.net/problem/14888
# 수열만들기 예시
# pool = ['A', 'B', 'C']
# print(list(map(''.join, permutations(pool)))) # 3개의 원소로 수열 만들기
# print(list(map(''.join, permutations(pool, 2)))) # 2개의 원소로 수열 만들기

from itertools import permutations

n = int(input())
nums = list(map(int, input().split()))
operatorCount = list(map(int, input().split()))
operators = []

for i in range(4):
    for j in range(operatorCount[i]):
        operators.append(i)

combi = list(permutations(operators))

total = 0
for arr in combi:
    index = 0
    total = nums[index]
    for op in arr:
        if op == 0:
            total += nums[index+1]
        elif op == 1:
            total -= nums[index + 1]
        elif op == 2:
            total *= nums[index + 1]
        elif op == 3:
            u = total
            v = nums[index+1]
            flag = False
            if u < 0 : # 음수일 경우 양수로 변환후 나누고 다시 음수 붙이기
                u *= -1
                flag = True
            if v < 0:
                v *= -1
                flag = True
            if flag:
                total = u // v
                total *= -1
            if u >0 and v > 0:
                nums[index] //= nums[index + 1]
        index += 2
    print(total)
