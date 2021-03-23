# 문자와 숫자가 섞여있는 문자열이 주어지면
# 그 중 숫자만 추출해서 그 순서대로 자연수 만들고
# 그 자연수의 약수의 개수를 구한다.
# 입력: g0en2Ts8eSoft
st = list(input())

# 문자열 안에서 숫자만 추출
numStr = ''
for ch in st:
    if ch.isdigit():
        numStr += str(ch)

# 추출한 문자 정수로 변환 : str->int 로 형변환
numStr = int(numStr)
print(numStr)

# 앞에 0이오는 경우 제거하면 정수만드는 로직
res = 0
for ch in st:
    if ch.isdigit():
       res = res * 10 + int(ch)

# 약수의 개수 구하기
cnt = 0

for i in range(1, numStr+1):
    if numStr % i ==0:
        cnt+=1
print(cnt)