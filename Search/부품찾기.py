# 부품찾기
# 입력
# 5
# 8 3 7 9 2 -> 기준 데이터
# 3
# 5 7 9     -> 찾으려는 데이터
# 정답: no yes yes

n = int(input())
arrN = list(map(int, input().split()))
arrN.sort()

m = int(input())
arrM = list(map(int, input().split()))

# 방법1 : 이진탐색
def binarySearch(arr, start, end, target):
    if start > end:
        return None
    mid = (start + end) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binarySearch(arr, start, mid-1, target)
    else:
        return binarySearch(arr, mid+1, end, target)

for i in arrM:
    if binarySearch(arrN, 0, len(arrN)-1, i) == None:
        print('no', end=' ')
    else:
        print('yes', end=' ')

# 방법2 : 계수 정렬 풀이
arr = [0] * (max(arrN)+1)

for i in arrN:
    arr[i] += 1

for i in arrM:
    if arr[i] == 0:
        print('no', end=' ')
    else:
        print('yes', end=' ')

# 방법3 : set 자료구조 풀이
arrN2 = set(map(int, input().split()))

for i in arrM:
    if i in arrN2:
        print('yes', end=' ')
    else:
        print('no', end=' ')