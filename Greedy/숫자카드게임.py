# 가장 높은 숫자가 쓰인 카드를 1장 뽑는 게임.
# 게임규칙
# 1. N x M 형태로 카드가 놓여있다.
# 2. 한 행을 선택해 그 안에서 가장 작은 숫자카드를 고른다.
# 3. 처음에 카드를 골라낼 행을 선택할때, 이후에 해당 행에서 가장 숫자가 낮은 카드를 뽑을 것을 고려하여
#    최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 전략을 세워라
# (1) 입력 및 정답 -> 2
# 3 3
# 3 1 2
# 4 1 4
# 2 2 2
#
# (2) 입력 및 정답 -> 3
# 2 4
# 7 3 1 8
# 3 3 3 4

n, m = map(int, input().split())
result = 0
for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(min_value, result)
print(result)


