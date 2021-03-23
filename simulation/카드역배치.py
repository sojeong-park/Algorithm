# 주어지는 구간에 맞춰 카드를 역배치한다. 리스트 안에서 swap

arr = [i for i in range(0, 21)]


for _ in range(10):
    a, b = map(int, input().split())
    for i in range((b-a+1)//2):
        arr[a+i], arr[b-i] = arr[b-i], arr[a+i]
arr.pop(0)
print(arr)