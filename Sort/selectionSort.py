# 선택 정렬
# 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸고,
# 그 다음 데이터를 선택해 앞에서 두번째 데이터와 바꾸는 과정 반복

arr = [7,5,9,0,3,1,6,2,4,8]

def selectionSort(arr):
    for i in range(len(arr)):
        minIndex = i
        for j in range(i+1, len(arr)):
            if arr[minIndex] > arr[j]:
                minIndex = j
        arr[i], arr[minIndex] = arr[minIndex], arr[i]

selectionSort(arr)
print(arr)