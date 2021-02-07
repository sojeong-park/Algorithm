# 떡볶이 떡 만들기 - 파라메트릭 서치 유형의 문제
# N 만큼의 떡의 개수가 주어지고 M 만큼의 떡을 얻기 위해 절단기에 설정할수 있는 높이의 최댓값을 구해라
# 1<=N<=1000000, 1<=M<=2000000000
# 절단기의 높이는 최대 10억보다 작거나 같은 양의 정수 또는 0
# 입력          정답 15
# 4 6
# 19 15 10 17

n, m = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = max(arr)
result = 0

while start <= end:
    sum = 0
    mid = (start + end) // 2

    for i in arr:
        if i > mid:
            sum += (i - mid)
    if sum < m:   # 양이 부족한 경우 왼쪽 탐색(더 자르기)
        end = mid -1
    else:           # 양이 충분한 경우 오른쪽 탐색(덜자르기)
        result = mid # 최대한 덜 잘랐을 때가 정답
        start = mid + 1

print(result)