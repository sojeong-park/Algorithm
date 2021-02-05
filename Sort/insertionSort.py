# 삽입정렬
# 특정한 데이터가 적절한 위치에 들어가기 이전에 그 앞까지의 데이터는 이미 정렬되어있다고 가정
# 정렬되어있는 리스트에서 적절한 위치를 찾은뒤 그 위치에 삽입

arr = [7,5,9,0,3,1,6,2,4,8]

def insertionSort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j-1] > arr[j]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else:
                break

insertionSort(arr)
print(arr)
