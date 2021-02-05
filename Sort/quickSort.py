# 퀵 정렬
arr = [7,5,9,0,3,1,6,2,4,8]

def quickSort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    tail = arr[1:]

    leftSide = [x for x in tail if x <= pivot]
    rightSide = [x for x in tail if x >= pivot]

    return quickSort(leftSide) + [pivot] + quickSort(rightSide)

print(quickSort(arr))