# 성적이 낮은순서로 이름 출력하기
# 입력
# 2
# 홍길동 90
# 이순신 77

n = int(input())
arr = []

for i in range(n):
    inputData = input().split()
    arr.append((inputData[0], int(inputData[1])))

arr = sorted(arr, key=lambda s: s[1])

for i in arr:
    print(i[0], end=" ")