# 규칙: n명 모험가의 공포도가 주어지는데 공포도 x인 모험가는 반드시 x명 이상으로 구성한 모험가 그룹에 참여해야 한다.
# 여행 떠날수 있는 그룹수의 최대값을 구해라.
# 항상 최소한의 모험가의 수를 포함하여야 최대한 많은 그룹이 구성된다
# 입력
# 5
# 1 2 3 2 2

n = int(input())
arr = list(map(int, input().split()))

count = 0 # 모험가의 수
group = 0 # 그룹 수

arr.sort()

for i in arr:
    count += 1 # 현재 그룹에 모험가 포함
    if count >= i: # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면 그룹 결성
        group += 1
        count = 0

print(group)