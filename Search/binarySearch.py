# 이진 탐색

# 재귀 구현
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

# 반복문 구현
def binarySearchWhile(arr, start, end, target):
    while start <= end :
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
arr = [1,2,3,4,5,6,7,8,9,10]

result = binarySearch(arr, 0, len(arr)-1, 2)
if result == None:
    print('값이 없습니다.');
else:
    print(result)

