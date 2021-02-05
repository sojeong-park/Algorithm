# 주어지는 수를 내림차순으로 정렬하라
# 입력 -> 정답: 27 15 12
# 3
# 15
# 27
# 12

n = int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))

arr.sort(reverse=True)
print(arr)

