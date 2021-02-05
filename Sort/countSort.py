# 계수정렬
# 원소들을 비교하지 않고 별도의 리스트를 선언하고 그 안에 정렬에 대한 정보를 담는다
# 양의 정수이면서 가장 큰 데이터와 가장 작은데이터의 차이가 적을 경우 계수 정렬 사용에 적합
# ex) 0 ~ 100 사이 시험성적 정렬

arr = [7,5,9,0,3,1,6,2,4,8,0,2,9,7,5]

count = [0] * (max(arr) + 1)

def countSort(arr):
    for i in arr:
        count[i] += 1
    for i in range(len(count)):
        for j in range(count[i]):
            print(i, end=' ')

countSort(arr)
